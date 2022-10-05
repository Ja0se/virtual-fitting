import copy
# net=infer.U2net()
# img=Image.open('./input_images/1234.jpg').convert('RGB')
# img=net.Output(img)

class Div:
  def __init__(self,img):
    self.img=img
    self.Width=img.width
    self.Height=img.height
  def Red(self):
    #128,0,0
    image=copy.deepcopy(self.img)
    x,y,w,h=self.Width,self.Height,0,0
    flag=False
    for i in range(self.Width):
      for j in range(self.Height):
        if self.img[i][j][0] is 128 and self.img[i][j][1] is 0 and self.img[i][j][2] is 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
          flag=True
        else:
          image[i][j][0],image[i][j][1],image[i][j][2]=0,0,0
    if flag is True:
      return x,y,w,h,image
    else:
      return 0,0,0,0,0
  def Green(self):
    image=copy.deepcopy(self.img)
    x,y,w,h=self.Width,self.Height,0,0
    flag=False
    for i in range(self.Width):
      for j in range(self.Height):
        if self.img[i][j][0] is 0 and self.img[i][j][1] is 128 and self.img[i][j][2] is 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
          flag=True
        else:
          image[i][j][0],image[i][j][1],image[i][j][2]=0,0,0
    if flag is True:
      return x,y,w,h,image
    else:
      return 0,0,0,0,0
  def Yellow(self):
    image=copy.deepcopy(self.img)
    x,y,w,h=self.Width,self.Height,0,0
    flag=False
    for i in range(self.Width):
      for j in range(self.Height):
        if self.img[i][j][0] is 128 and self.img[i][j][1] is 128 and self.img[i][j][2] is 0:
          x,y,w,h=min(i,x),min(j,y),max(i,w),max(j,h)
          flag=True
        else:
          image[i][j][0],image[i][j][1],image[i][j][2]=0,0,0
    if flag is True:
      return x,y,w,h,image
    else:
      return 0,0,0,0,0
  
