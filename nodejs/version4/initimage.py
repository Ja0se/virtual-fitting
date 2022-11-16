import sys
from PIL import Image
import cv2
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
from Make_Image import MI
from Extract_Color import Extract
import Color

def testFunc():
    f = open("./test.txt","r")
    read_data=f.read()
    f.close()
    img = Image.open(BytesIO(base64.b64decode(read_data)))
    img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    
    unet=MI(img)
    img=unet.Output()
    # upimage resize
    
    Ext=Extract()
    Ext.Clt(2)
    Ext.fit(img)
    Img,perc,k_cluster=Ext.palette_perc()
    centers=Ext.Centers()
    tmp=0
    if perc[0]<perc[1]:
        tmp=1
    color=Color.Colorfull(centers[tmp])
    jpg_img = cv2.imencode('.jpg', img)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    d= open("./test.txt","w")
    d.write(str(b64_string))
    d.close()
    arr=['white','red','orange','yellow','light green','green','khaki','brown','black','grey','pink','purple','blue','sky blue','indigo','beige','ivory']
    
    return str(arr[int(color)]).split('\\')[0]
    
if __name__ == '__main__':
    print(testFunc())