import Make_Image
import infer
import Extract_Color
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import Divide
import copy
import cv2

def imgshow(img):
    plt.figure()
    plt.imshow(img)
    plt.show()
    
if __name__== '__main__':
    net = infer.U2net()
    Ext=Extract_Color.Extract()
    img_path='./input_images/11.jpg'
    img=Image.open(img_path).convert('RGB')
    '''
    Extract Color using unet c_model
    '''
    unet=Make_Image.MI(img_path)
    unet_mask=unet.Output()
    Ext.Clt(4)
    Ext.fit(unet_mask)
    ExtractImg,perc,k_cluster=Ext.palette_perc()
    #imgshow(ExtractImg)
    #imgshow(img)
    '''
    Divide clothes using u2net
    '''
    u2net_mask=net.Output(img)
    u2net_mask=u2net_mask.convert('RGB')
    #print(u2net_mask)
    # 이거 그거 이미지 디코딩 작업해야할듯
    #imgshow(u2net_mask)
    
    
    Div=Divide.Div(u2net_mask,img)
    x,y,w,h,Div_image=Div.Red()
    print(x,y,w,h)
    #print(Div_image)
    if(Div_image is not 0):
        Div_image=Div_image[x:w,y:h]
        imgshow(Div_image)
        
    Ext.fit(Div_image)
    ExtractImg,perc,k_cluster=Ext.palette_perc()
    imgshow(ExtractImg)
    print(perc,k_cluster)
