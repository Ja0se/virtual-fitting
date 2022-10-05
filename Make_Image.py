import numpy as np
import cv2
import torch
import albumentations as albu
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os
import glob
from iglovikov_helper_functions.utils.image_utils import load_rgb, pad, unpad
from iglovikov_helper_functions.dl.pytorch.utils import tensor_from_rgb_image
from people_segmentation.pre_trained_models import create_model as p_create_model
from cloths_segmentation.pre_trained_models import create_model as c_create_model
import PIL
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
class MI:
  def __init__(self,image_path):
    #read model
    self.p_model = p_create_model("Unet_2020-07-20")#people segmentation
    self.c_model = c_create_model("Unet_2020-10-30")#clothes segmentation
    self.p_model.eval();
    self.c_model.eval();
    #read image
    self.image_path=image_path
    self.image=load_rgb(image_path)
  def Output(self):
    #clothes masking
    transform = albu.Compose([albu.Normalize(p=1)], p=1)
    padded_image, pads = pad(self.image, factor=32, border=cv2.BORDER_CONSTANT)
    x = transform(image=padded_image)["image"]
    x = torch.unsqueeze(tensor_from_rgb_image(x), 0)
    with torch.no_grad():
      prediction = self.c_model(x)[0][0]
    mask = (prediction > 0).cpu().numpy().astype(np.uint8)
    mask = unpad(mask, pads)

    masked=cv2.bitwise_and(self.image,cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB) * 255)
    #masked=cv2.resize(masked,(427,367))
    return masked
    '''
    Extract Color
    Using KMeans
    cluster number = 4
    perc[0] is back ground -> using data start 1
    '''
# import Extract_Color

# Ext=Extract_Color.Extract()
# Ext.Clt(4)
# Ext.fit(masked)
# Img,perc,k_cluster=Ext.palette_perc()

# print(perc)
# print(Ext.Centers())

# return

# plt.figure()
# plt.imshow(Img)
# plt.show()
