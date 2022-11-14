import sys
from PIL import Image
import cv2
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

def testFunc():
    f = open("./nodejs/test.txt","r")
    read_data=f.read()
    f.close()
    img = Image.open(BytesIO(base64.b64decode(read_data)))
    img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    data=base64.b64encode(img)
    d= open("./nodejs/test.txt","w")
    d.write(str(data))
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