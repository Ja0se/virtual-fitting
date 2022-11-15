import numpy as np
import cv2
import torch
import albumentations as albu
import matplotlib.pyplot as plt
from iglovikov_helper_functions.utils.image_utils import pad, unpad
from iglovikov_helper_functions.dl.pytorch.utils import tensor_from_rgb_image
from people_segmentation.pre_trained_models import create_model as p_create_model
from cloths_segmentation.pre_trained_models import create_model as c_create_model
from PIL import Image
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class MI:
  def __init__(self,image_path):
    #read model
    self.c_model = c_create_model("Unet_2020-10-30")#clothes segmentation
    self.c_model.eval();
    #read image
    self.image= cv2.cvtColor(np.array(image_path), cv2.COLOR_BGR2RGB)
    
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
    # 사람 사이즈에 맞춰서 resize
    
    Height,Width,Color=masked.shape
    x,y,w,h=Width,Height,0,0
    for j in range(Width):
      for i in range(Height):
        if masked[i][j][0] != 0 or masked[i][j][1] != 0 or masked[i][j][2] != 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
    masked=masked[x:w,y:h]
    return masked
  
    
    '''
    Extract Color
    Using KMeans
    cluster number = 4
    perc[0] is back ground -> using data start 1
    '''
    
if __name__ == "__main__":
  # f = open("./test.txt","r")
  # read_data=f.read()
  # f.close()
  # #decode
  # img = Image.open(BytesIO(base64.b64decode(read_data)))
  # img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
  # plt.imshow(img)
  # plt.show()
  
  img=cv2.imread('./input_images/13.jpg')
  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  plt.imshow(img)
  plt.show()
  
  unet=MI(img)
  plt.figure()
  maked=unet.Output()
  plt.imshow(maked)
  plt.show()
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