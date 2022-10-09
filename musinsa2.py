import re
import time
import base64
import requests
import numpy as np
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import Make_Image
import infer
import Extract_Color
import matplotlib.pyplot as plt
import Divide
import copy
import cv2
import Color
import recommend_weight as rw
check = False

options = Options()
# options.add_argument()
net = infer.U2net()
Ext=Extract_Color.Extract()

url = 'https://www.musinsa.com/mz/brandsnap'
# s = Service('./chromedriver.exe')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url)

totalPage = driver.find_element(By.CLASS_NAME, 'totalPagingNum').text
totalPage = re.findall('\d+', totalPage)
totalPage = int(''.join(totalPage))

totalImg = []

for item in range(totalPage//10-1):
    pageBox = driver.find_elements(By.CSS_SELECTOR, '.pagination > div > a')
    for idx in range(2, 12):
        pageBox[idx].send_keys('\n')
        time.sleep(1)
        imgList = driver.find_elements(By.CSS_SELECTOR, '.articleImg > a > img')
        
        for img in imgList:
            #totalImg.append(base64.b64encode(requests.get(img.get_attribute('src')).content))
            # totalImg.append(img.get_attribute('src'))
            res = requests.get(img.get_attribute('src'))
            img = Image.open(BytesIO(res.content))
            npimg = np.array(img)
            #print(npimg)
            '''
            test 시작
            '''
            u2net_mask=net.Output(img)
            u2net_mask=u2net_mask.convert('RGB')
            Up,Bottom,Outer=-1,-1,-1
            
            plt.figure()
            plt.imshow(u2net_mask)
            plt.show()
            
            Div=Divide.Div(u2net_mask,img)
            #상의 추출
            x,y,w,h,Div_image=Div.Red()
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
            
            #외투 추출
            x,y,w,h,Div_image=Div.Yellow()
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
                Outer=Color.Colorfull(k_cluster.cluster_centers_[mask_color])
            
            rw.Add(Up,Bottom,Outer)
            print(Up,Bottom,Outer)
            '''
            test 끝
            '''
        pageBox = driver.find_elements(By.CSS_SELECTOR, '.pagination > div > a')
    pageBox[12].send_keys('\n')
    time.sleep(1)

driver.quit()
