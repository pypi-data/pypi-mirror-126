# Copyright (c) OpenMMLab. All rights reserved.
import numbers
import os.path as osp

import mmcv
import torch

from mmedit.core import tensor2img
from ..builder import build_backbone, build_component, build_loss
from ..common import set_requires_grad
from ..registry import MODELS
from .basic_restorer import BasicRestorer


@MODELS.register_module()
class TTSR(BasicRestorer):
    """TTSR model for Reference-based Image Super-Resolution.

    Paper: Learning Texture Transformer Network for Image Super-Resolution.

    Args:
        generator (dict): Config for the generator.
        extractor (dict): Config for the extractor.
        transformer (dict): Config for the transformer.
        pixel_loss (dict): Config for the pixel loss.
        discriminator (dict): Config for the discriminator. Default: None.
        perceptual_loss (dict): Config for the perceptual loss. Default: None.
        transferal_perceptual_loss (dict): Config for the transferal perceptual
            loss. Default: None.
        gan_loss (dict): Config for the GAN loss. Default: None
        train_cfg (dict): Config for train. Default: None.
        test_cfg (dict): Config for testing. Default: None.
        pretrained (str): Path for pretrained model. Default: None.
    """

    def __init__(self,
                 generator,
                 extractor,
                 transformer,
                 pixel_loss,
                 discriminator=None,
                 perceptual_loss=None,
                 transferal_perceptual_loss=None,
                 gan_loss=None,
                 train_cfg=None,
                 test_cfg=None,
                 pretrained=None):
        super(BasicRestorer, self).__init__()

        self.train_cfg = train_cfg
        self.test_cfg = test_cfg

        # model
        self.generator = build_backbone(generator)
        self.transformer = build_component(transformer)
        self.extractor = build_component(extractor)
        # discriminator
        if discriminator and gan_loss:
            self.discriminator = build_component(discriminator)
            self.gan_loss = build_loss(gan_loss)
        else:
            self.discriminator = None
            self.gan_loss = None

        # loss
        self.pixel_loss = build_loss(pixel_loss)
        self.perceptual_loss = build_loss(
            perceptual_loss) if perceptual_loss else None
        if transferal_perceptual_loss:
            self.transferal_perceptual_loss = build_loss(
                transferal_perceptual_loss)
        else:
            self.transferal_perceptual_loss = None
        # pretrained
        self.init_weights(pretrained)

        # fix pre-trained networks
        self.register_buffer('step_counter', torch.zeros(1))
        self.fix_iter = train_cfg.get('fix_iter', 0) if train_cfg else 0
        self.disc_steps = train_cfg.get('disc_steps', 1) if train_cfg else 1

    def forward_dummy(self, lq, lq_up, ref, ref_downup, only_pred=True):
        """Forward of networks.

        Args:
            lq (Tensor): LQ image.
            lq_up (Tensor): Upsampled LQ image.
            ref (Tensor): Reference image.
            ref_downup (Tensor): Image generated by sequentially applying
                bicubic down-sampling and up-sampling on reference image.
            only_pred (bool): Only return predicted results or not.
                Default: True.

        Returns:
            pred (Tensor): Predicted super-resolution results (n, 3, 4h, 4w).
            soft_attention (Tensor): Soft-Attention tensor with shape
                (n, 1, h, w).
            textures (Tuple[Tensor]): Transferred GT textures.
                [(N, C, H, W), (N, C/2, 2H, 2W), ...]
        """

        lq_up, _, _ = self.extractor(lq_up)
        ref_downup, _, _ = self.extractor(ref_downup)
        refs = self.extractor(ref)

        soft_attention, textures = self.transformer(lq_up, ref_downup, refs)

        pred = self.generator(lq, soft_attention, textures)

        if only_pred:
            return pred
        return pred, soft_attention, textures

    def forward(self, lq, gt=None, test_mode=False, **kwargs):
        """Forward function.

        Args:
            lq (Tensor): Input lq images.
            gt (Tensor): Ground-truth image. Default: None.
            test_mode (bool): Whether in test mode or not. Default: False.
            kwargs (dict): Other arguments.
        """

        if test_mode:
            return self.forward_test(lq, gt=gt, **kwargs)

        return self.forward_dummy(lq, **kwargs)

    def train_step(self, data_batch, optimizer):
        """Train step.

        Args:
            data_batch (dict): A batch of data, which requires
                'lq', 'gt', 'lq_up', 'ref', 'ref_downup'
            optimizer (obj): Optimizer.

        Returns:
            dict: Returned output, which includes:
                log_vars, num_samples, results (lq, gt and pred).

        """
        # data
        lq = data_batch['lq']
        lq_up = data_batch['lq_up']
        gt = data_batch['gt']
        ref = data_batch['ref']
        ref_downup = data_batch['ref_downup']

        # generate
        pred, soft_attention, textures = self(
            lq, lq_up=lq_up, ref=ref, ref_downup=ref_downup, only_pred=False)

        # loss
        losses = dict()
        log_vars = dict()

        # no updates to discriminator parameters.
        set_requires_grad(self.discriminator, False)

        losses['loss_pix'] = self.pixel_loss(pred, gt)
        if self.step_counter >= self.fix_iter:
            # perceptual loss
            if self.perceptual_loss:
                loss_percep, loss_style = self.perceptual_loss(pred, gt)
                if loss_percep is not None:
                    losses['loss_perceptual'] = loss_percep
                if loss_style is not None:
                    losses['loss_style'] = loss_style
            if self.transferal_perceptual_loss:
                set_requires_grad(self.extractor, False)
                sr_textures = self.extractor((pred + 1.) / 2.)
                losses['loss_transferal'] = self.transferal_perceptual_loss(
                    sr_textures, soft_attention, textures)
            # gan loss for generator
            if self.gan_loss:
                fake_g_pred = self.discriminator(pred)
                losses['loss_gan'] = self.gan_loss(
                    fake_g_pred, target_is_real=True, is_disc=False)

        # parse loss
        loss_g, log_vars_g = self.parse_losses(losses)
        log_vars.update(log_vars_g)

        # optimize
        optimizer['generator'].zero_grad()
        loss_g.backward()
        optimizer['generator'].step()

        if self.discriminator and self.step_counter >= self.fix_iter:
            # discriminator
            set_requires_grad(self.discriminator, True)
            for _ in range(self.disc_steps):
                # real
                real_d_pred = self.discriminator(gt)
                loss_d_real = self.gan_loss(
                    real_d_pred, target_is_real=True, is_disc=True)
                loss_d, log_vars_d = self.parse_losses(
                    dict(loss_d_real=loss_d_real))
                optimizer['discriminator'].zero_grad()
                loss_d.backward()
                log_vars.update(log_vars_d)
                # fake
                fake_d_pred = self.discriminator(pred.detach())
                loss_d_fake = self.gan_loss(
                    fake_d_pred, target_is_real=False, is_disc=True)
                loss_d, log_vars_d = self.parse_losses(
                    dict(loss_d_fake=loss_d_fake))
                loss_d.backward()
                log_vars.update(log_vars_d)

                optimizer['discriminator'].step()

        log_vars.pop('loss')  # remove the unnecessary 'loss'
        outputs = dict(
            log_vars=log_vars,
            num_samples=len(gt.data),
            results=dict(
                lq=lq.cpu(), gt=gt.cpu(), ref=ref.cpu(), output=pred.cpu()))

        self.step_counter += 1

        return outputs

    def forward_test(self,
                     lq,
                     lq_up,
                     ref,
                     ref_downup,
                     gt=None,
                     meta=None,
                     save_image=False,
                     save_path=None,
                     iteration=None):
        """Testing forward function.

        Args:
            lq (Tensor): LQ image
            gt (Tensor): GT image
            lq_up (Tensor): Upsampled LQ image
            ref (Tensor): Reference image
            ref_downup (Tensor): Image generated by sequentially applying
                bicubic down-sampling and up-sampling on reference image
            meta (list[dict]): Meta data, such as path of GT file.
                Default: None.
            save_image (bool): Whether to save image. Default: False.
            save_path (str): Path to save image. Default: None.
            iteration (int): Iteration for the saving image name.
                Default: None.

        Returns:
            dict: Output results, which contain either key(s)
                1. 'eval_result'.
                2. 'lq', 'pred'.
                3. 'lq', 'pred', 'gt'.
        """

        # generator
        with torch.no_grad():
            pred = self.forward_dummy(
                lq=lq, lq_up=lq_up, ref=ref, ref_downup=ref_downup)

        pred = (pred + 1.) / 2.
        if gt is not None:
            gt = (gt + 1.) / 2.

        if self.test_cfg is not None and self.test_cfg.get('metrics', None):
            assert gt is not None, (
                'evaluation with metrics must have gt images.')
            results = dict(eval_result=self.evaluate(pred, gt))
        else:
            results = dict(lq=lq.cpu(), output=pred.cpu())
            if gt is not None:
                results['gt'] = gt.cpu()

        # save image
        if save_image:
            if 'gt_path' in meta[0]:
                the_path = meta[0]['gt_path']
            else:
                the_path = meta[0]['lq_path']
            folder_name = osp.splitext(osp.basename(the_path))[0]
            if isinstance(iteration, numbers.Number):
                save_path = osp.join(save_path, folder_name,
                                     f'{folder_name}-{iteration + 1:06d}.png')
            elif iteration is None:
                save_path = osp.join(save_path, f'{folder_name}.png')
            else:
                raise ValueError('iteration should be number or None, '
                                 f'but got {type(iteration)}')
            mmcv.imwrite(tensor2img(pred), save_path)

        return results

    def init_weights(self, pretrained=None, strict=True):
        """Init weights for models.

        Args:
            pretrained (str, optional): Path for pretrained weights. If given
                None, pretrained weights will not be loaded. Defaults to None.
            strict (boo, optional): Whether strictly load the pretrained model.
                Defaults to True.
        """
        if isinstance(pretrained, str):
            if self.generator:
                self.generator.init_weights(pretrained, strict)
            if self.extractor:
                self.extractor.init_weights(pretrained, strict)
            if self.transformer:
                self.transformer.init_weights(pretrained, strict)
        elif pretrained is not None:
            raise TypeError('"pretrained" must be a str or None. '
                            f'But received {type(pretrained)}.')
