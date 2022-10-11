import copy
import numpy as np
# net=infer.U2net()
# img=Image.open('./input_images/1234.jpg').convert('RGB')
# img=net.Output(img)

class Div:
  def __init__(self,img,normal):
    self.normal=np.array(normal)
    self.img=np.array(img)
    self.Width=img.width
    self.Height=img.height
  def Red(self):
    #128,0,0
    image=copy.deepcopy(self.img)
    x,y,w,h=self.Width,self.Height,0,0
    flag=False
    for j in range(self.Width):
      for i in range(self.Height):
        if image[i][j][0] == 128 and image[i][j][1] == 0 and image[i][j][2] == 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
          image[i][j][0],image[i][j][1],image[i][j][2]=self.normal[i][j][0],self.normal[i][j][1],self.normal[i][j][2]
          flag=True
        else:
          image[i][j][0],image[i][j][1],image[i][j][2]=0,0,0
    if flag == True:
      return x,y,w,h,image
    else:
      return 0,0,0,0,0
  def Green(self):
    image=copy.deepcopy(self.img)
    x,y,w,h=self.Width,self.Height,0,0
    flag=False
    for j in range(self.Width):
      for i in range(self.Height):
        if image[i][j][0] == 0 and image[i][j][1] == 128 and image[i][j][2] == 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
          image[i][j][0],image[i][j][1],image[i][j][2]=self.normal[i][j][0],self.normal[i][j][1],self.normal[i][j][2]
          flag=True
        else:
          image[i][j][0],image[i][j][1],image[i][j][2]=0,0,0
    if flag == True:
      return x,y,w,h,image
    else:
      return 0,0,0,0,0
  def Yellow(self):
    image=copy.deepcopy(self.img)
    x,y,w,h=self.Width,self.Height,0,0
    flag=False
    for j in range(self.Width):
      for i in range(self.Height):
        if image[i][j][0] == 128 and image[i][j][1] == 128 and image[i][j][2] == 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
          image[i][j][0],image[i][j][1],image[i][j][2]=self.normal[i][j][0],self.normal[i][j][1],self.normal[i][j][2]
          flag=True
        else:
          image[i][j][0],image[i][j][1],image[i][j][2]=0,0,0
    if flag == True:
      return x,y,w,h,image
    else:
      return 0,0,0,0,0
  