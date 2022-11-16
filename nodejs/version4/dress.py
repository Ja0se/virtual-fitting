import sys
from PIL import Image
import cv2
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

def testFunc(upwidth,neck,neckx):
    upwidth,neck,neckx=int(upwidth),int(neck),int(neckx)
    f = open("./dress.txt","r")
    read_data=f.read()
    f.close()
    dressimg = Image.open(BytesIO(base64.b64decode(read_data)))
    dressimg= cv2.cvtColor(np.array(dressimg), cv2.COLOR_BGR2RGB)
    
    # upimage resize
    Height,Width,Color=dressimg.shape
    gap=upwidth/Width
    Width=upwidth
    Height=int(Height*gap)
    dressimg=cv2.resize(dressimg,(Width,Height))
    
    f = open("./fit.txt","r")
    read_data=f.read()
    f.close()
    fitimg = Image.open(BytesIO(base64.b64decode(read_data)))
    fitimg= cv2.cvtColor(np.array(fitimg), cv2.COLOR_BGR2RGB)
    
    
    x=int(neckx-int(upwidth/2.))
    y=neck
    for j in range(Width):
        for i in range(Height):
            if(dressimg[i][j][0]!=0 or dressimg[i][j][1]!=0 or dressimg[i][j][2]!=0):
                fitimg[y+i][x+j]=dressimg[i][j]
    #encode
    
    jpg_img = cv2.imencode('.jpg', fitimg)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    d= open("./fit.txt","w")
    d.write(str(b64_string))
    d.close()
    return 'success'
    
if __name__ == '__main__':
    print(testFunc(sys.argv[1],sys.argv[2],sys.argv[3]))
    #print(testFunc(180,87,275))