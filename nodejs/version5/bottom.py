import sys
from PIL import Image
import cv2
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
from profile import MI2

def testFunc(pelvis,pelvisx,bottomwidth,bottom):
    pelvis,pelvisx,bottomwidth,bottom=int(pelvis)-50,int(pelvisx),int(bottomwidth),int(bottom)
    f = open("./bottom.txt","r")
    read_data=f.read()
    f.close()
    bottomimg = Image.open(BytesIO(base64.b64decode(read_data)))
    bottomimg= cv2.cvtColor(np.array(bottomimg), cv2.COLOR_BGR2RGB)
    
    # upimage resize
    Height,Width,Color=bottomimg.shape
    gap=bottomwidth/Width
    Width=bottomwidth
    Height=int(Height*gap)+40
    if Height>int(bottom-pelvis):
        Height=int(bottom-pelvis)
    bottomimg=cv2.resize(bottomimg,(Width,Height))
    
    f = open("./fit.txt","r")
    read_data=f.read()
    f.close()
    fitimg = Image.open(BytesIO(base64.b64decode(read_data)))
    fitimg= cv2.cvtColor(np.array(fitimg), cv2.COLOR_BGR2RGB)
    
    
    x=int(pelvisx-int(bottomwidth/2.))
    y=pelvis-50
    for j in range(Width):
        for i in range(Height):
            fitimg[y+i][x+j]=bottomimg[i][j]
    #encode
    
    jpg_img = cv2.imencode('.jpg', fitimg)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    d= open("./fit.txt","w")
    d.write(str(b64_string))
    d.close()
    return 'success'
    
if __name__ == '__main__':
    print(testFunc(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]))
    #print(testFunc(291,275,411,494))