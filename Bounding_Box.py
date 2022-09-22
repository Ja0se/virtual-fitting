import cv2
import os
import matplotlib.pyplot as plt

img='output_images/1163.png'
img=cv2.imread(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# red top 128,0,0
# blue pants 0,128,0
# yellow dress 128,128,0
height,width,_=img.shape

rx,ry,bx,by,yx,yy=width,height,width,height,width,height
rw,rh,bw,bh,yw,yh=0,0,0,0,0,0

flagr,flagb,flagy=False,False,False
for i in range(height):
    for j in range(width):
        if(img[i][j][0]==128 and img[i][j][1]==0 and img[i][j][2]==0):
            rx,ry,rw,rh=min(i,rx),min(ry,j),max(i,rw),max(j,rh)  
            flagr=True
        elif(img[i][j][0]==00 and img[i][j][1]==128 and img[i][j][2]==0):
            bx,by,bw,bh=min(i,bx),min(by,j),max(i,bw),max(j,bh)
            flagb=True
        elif(img[i][j][0]==128 and img[i][j][1]==128 and img[i][j][2]==0):
            yx,yy,yw,yh=min(i,yx),min(yy,j),max(i,yw),max(j,yh)
            flagy=True

if(flagr==True and flagb==False and flagy==False):
    cv2.rectangle(img,(ry,rx),(rh,rw),(255,0,0),3)  
elif(flagb==True and flagr==False and flagy==False):
    cv2.rectangle(img,(by,bx),(bh,bw),(0,255,0),3)
elif(flagy==True and flagb==False and flagr==False):
    cv2.rectangle(img,(yy,yx),(yh,yw),(255,255,0),3)
elif(flagr==True and flagb==True and flagy==False):
    if(rw-rx>bw-bx):
        cv2.rectangle(img,(ry,rx),(rh,rw),(255,0,0),3)  
    else:
        cv2.rectangle(img,(by,bx),(bh,bw),(0,255,0),3)    
elif(flagr==True and flagy==True and flagb==False):
    if(rw-rx>yw-yx):
        cv2.rectangle(img,(ry,rx),(rh,rw),(255,0,0),3)  
    else:   
        cv2.rectangle(img,(yy,yx),(yh,yw),(255,255,0),3)    
elif(flagy==True and flagb==True and flagr==False):
    if(bw-bx>yw-yx):
        cv2.rectangle(img,(by,bx),(bh,bw),(0,255,0),3)    
    else:   
        cv2.rectangle(img,(yy,yx),(yh,yw),(255,255,0),3)    
elif(flagr==True and flagb==True and flagy==True):
    if(rw-rx>bw-bx and rw-rx>yw-yx):
        cv2.rectangle(img,(ry,rx),(rh,rw),(255,0,0),3)  
    elif(bw-bx>rw-rx and bw-bx>yw-yx):
        cv2.rectangle(img,(by,bx),(bh,bw),(0,255,0),3)    
    else:
        cv2.rectangle(img,(yy,yx),(yh,yw),(255,255,0),3)    
        
plt.figure()
plt.imshow(img)
plt.show()
''' 
앱에서 찍는 이미지의 경우 가장 박스가 큰 하나만 처리하는 방식이 좋을듯
'''