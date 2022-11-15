import sys
from PIL import Image
import cv2
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
from profile import MI2

def testFunc(neck,neckx,upwidth,pelvis):
    f = open("./up.txt","r")
    neck,neckx,upwidth,pelvis=int(neck),int(neckx),int(upwidth),int(pelvis)
    read_data=f.read()
    f.close()
    upimg = Image.open(BytesIO(base64.b64decode(read_data)))
    upimg= cv2.cvtColor(np.array(upimg), cv2.COLOR_BGR2RGB)
    
    # upimage resize
    Height,Width,Color=upimg.shape
    Width=upwidth
    Height=int(pelvis-neck)
    upimg=cv2.resize(upimg,(Width,Height))
    
    f = open("./fit.txt","r")
    read_data=f.read()
    f.close()
    fitimg = Image.open(BytesIO(base64.b64decode(read_data)))
    fitimg= cv2.cvtColor(np.array(fitimg), cv2.COLOR_BGR2RGB)
    
    
    x=int(neckx-int(upwidth/2.))
    y=neck
    for j in range(Width):
        for i in range(Height):
            fitimg[y+i][x+j]=upimg[i][j]
    #encode
    
    jpg_img = cv2.imencode('.jpg', fitimg)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    d= open("./fit.txt","w")
    d.write(str(b64_string))
    d.close()
    return 'success'
    
if __name__ == '__main__':
    print(testFunc(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]))