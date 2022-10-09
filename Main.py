import Make_Image
import infer
import Extract_Color
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import Divide
import copy
import cv2
import Color
def imgshow(img):
    plt.figure()
    plt.imshow(img)
    plt.show()
    
if __name__== '__main__':
    Up,Bottom,Dress=-1,-1,-1
    net = infer.U2net()
    Ext=Extract_Color.Extract()
    img_path='./input_images/1416.jpg'
    img=Image.open(img_path).convert('RGB')
    '''
    Extract Color using unet c_model
    '''
    unet=Make_Image.MI(img_path)
    unet_mask=unet.Output()
    Ext.Clt(2)
    Ext.fit(unet_mask)
    ExtractImg,perc,k_cluster=Ext.palette_perc()
    #imgshow(ExtractImg)
    #imgshow(img)
    '''
    Divide clothes using u2net
    '''
    u2net_mask=net.Output(img)
    u2net_mask=u2net_mask.convert('RGB')
    imgshow(u2net_mask)
    Div=Divide.Div(u2net_mask,img)
    #상의 추출
    x,y,w,h,Div_image=Div.Red()
    print(x,y,w,h)
    #print(Div_image)
    if(Div_image is not 0):
        Div_image=Div_image[x:w,y:h]
        Ext.fit(Div_image)
        ExtractImg,perc,k_cluster=Ext.palette_perc()
        mask_color=0
        if perc[0]>perc[1]:
            mask_color=0
        else:
            mask_color=1
        #print(perc[mask_color])
        #print(k_cluster.cluster_centers_[mask_color])
        Up=Color.Colorfull(k_cluster.cluster_centers_[mask_color])
    
    #하의 추출
    x,y,w,h,Div_image=Div.Green()
    print(x,y,w,h)
    #print(Div_image)
    if(Div_image is not 0):
        Div_image=Div_image[x:w,y:h]
        Ext.fit(Div_image)
        ExtractImg,perc,k_cluster=Ext.palette_perc()
        mask_color=0
        if perc[0]>perc[1]:
            mask_color=0
        else:
            mask_color=1
        #print(perc[mask_color])
        #print(k_cluster.cluster_centers_[mask_color])
        Bottom=Color.Colorfull(k_cluster.cluster_centers_[mask_color])
    
    #dress 추출
    x,y,w,h,Div_image=Div.Yellow()
    print(x,y,w,h)
    #print(Div_image)
    if(Div_image is not 0):
        Div_image=Div_image[x:w,y:h]
        Ext.fit(Div_image)
        ExtractImg,perc,k_cluster=Ext.palette_perc()
        mask_color=0
        if perc[0]>perc[1]:
            mask_color=0
        else:
            mask_color=1
        #print(perc[mask_color])
        #print(k_cluster.cluster_centers_[mask_color])
        Dress=Color.Colorfull(k_cluster.cluster_centers_[mask_color])
        
    print(Up,Bottom,Dress)
