import sys
from PIL import Image
import cv2
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
from Make_Image import MI

def testFunc():
    f = open("./test.txt","r")
    read_data=f.read()
    f.close()
    #decode
    img = Image.open(BytesIO(base64.b64decode(read_data)))
    img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    
    #clothes background delete
    unet= MI(img)
    masked=unet.Output()
    
    #encode
    jpg_img = cv2.imencode('.jpg', masked)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    d= open("./test.txt","w")
    d.write(str(b64_string))
    d.close()
    return 'success'
    # return 'hi'
    #data=data.form['data']
    # imgdata = base64.b64decode(data)
    # dataBytesIO = io.BytesIO(imgdata)
    # image = Image.open(dataBytesIO)
    # return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    
if __name__ == '__main__':
    #print(testFunc(sys.argv[1]))
    print(testFunc())