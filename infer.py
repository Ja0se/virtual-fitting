import os

from tqdm import tqdm
from PIL import Image
import numpy as np

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import torch
import torch.nn.functional as F
import torchvision.transforms as transforms

from data.base_dataset import Normalize_image
from utils.saving_utils import load_checkpoint_mgpu

from networks import U2NET

class U2net:
    def __init__(self):
        self.device = "cpu"

        self.image_dir = "input_images"
        self.result_dir = "output_images"
        self.checkpoint_path = os.path.join("trained_checkpoint", "cloth_segm_u2net_latest.pth")
        self.do_palette = True
        self.net = U2NET(in_ch=3, out_ch=4)
        self.net = load_checkpoint_mgpu(self.net, self.checkpoint_path)
        self.net = self.net.to(self.device)
        self.net = self.net.eval()

    def get_palette(self,num_cls):
        """Returns the color map for visualizing the segmentation mask.
        Args:
            num_cls: Number of classes
        Returns:
            The color map
        """
        n = num_cls
        palette = [0] * (n * 3)
        for j in range(0, n):
            lab = j
            palette[j * 3 + 0] = 0
            palette[j * 3 + 1] = 0
            palette[j * 3 + 2] = 0
            i = 0
            while lab:
                palette[j * 3 + 0] |= ((lab >> 0) & 1) << (7 - i)
                palette[j * 3 + 1] |= ((lab >> 1) & 1) << (7 - i)
                palette[j * 3 + 2] |= ((lab >> 2) & 1) << (7 - i)
                i += 1
                lab >>= 3
        return palette

    def Output(self,image):

        transforms_list = []
        transforms_list += [transforms.ToTensor()]
        transforms_list += [Normalize_image(0.5, 0.5)]
        transform_rgb = transforms.Compose(transforms_list)

        palette = self.get_palette(4)

        image_tensor=transform_rgb(image)
        image_tensor=torch.unsqueeze(image_tensor,0)
        output_tensor = self.net(image_tensor.to(self.device))
        output_tensor = F.log_softmax(output_tensor[0], dim=1)
        output_tensor = torch.max(output_tensor, dim=1, keepdim=True)[1]
        output_tensor = torch.squeeze(output_tensor, dim=0)
        output_tensor = torch.squeeze(output_tensor, dim=0)
        output_arr = output_tensor.cpu().numpy()
        output_img = Image.fromarray(output_arr.astype("uint8"), mode="L")
        if self.do_palette:
            output_img.putpalette(palette)
        #output_img.save(os.path.join(result_dir, image_name[:-3] + "png"))
        return output_img
    
        # images_list = sorted(os.listdir(image_dir))
        # pbar = tqdm(total=len(images_list))
        # for image_name in images_list:
        #     img = Image.open(os.path.join(image_dir, image_name)).convert("RGB")
        #     image_tensor = transform_rgb(img)
        #     image_tensor = torch.unsqueeze(image_tensor, 0)

        #     output_tensor = net(image_tensor.to(device))
        #     output_tensor = F.log_softmax(output_tensor[0], dim=1)
        #     output_tensor = torch.max(output_tensor, dim=1, keepdim=True)[1]
        #     output_tensor = torch.squeeze(output_tensor, dim=0)
        #     output_tensor = torch.squeeze(output_tensor, dim=0)
        #     output_arr = output_tensor.cpu().numpy()

        #     output_img = Image.fromarray(output_arr.astype("uint8"), mode="L")
        #     if do_palette:
        #         output_img.putpalette(palette)
        #     output_img.save(os.path.join(result_dir, image_name[:-3] + "png"))

        #     pbar.update(1)

        # pbar.close()

'''
we need change these code to class
return one output image
'''
