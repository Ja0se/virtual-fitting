import sys
import numpy as np
import pandas as pd
def testFunc(color):    
    color=str(color)
    df=pd.read_csv('up_bottom.csv')
    if(color=='white'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='red'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='orange'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='yellow'):
        return 'color=\'ivory\' or color = \'red\' or color = \'brown\' order by rand() limit 2'
    elif(color=='lightgreen'):
        return 'color=\'ivory\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='green'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='khaki'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='brown'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='black'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='grey'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='pink'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='purple'):
        return 'color=\'grey\' or color = \'black\' or color = \'blue\' order by rand() limit 2'
    elif(color=='blue'):
        return 'color=\'grey\' or color = \'black\' or color = \'blue\' order by rand() limit 2'
    elif(color=='skyblue'):
        return 'color=\'grey\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='indigo'):
        return 'color=\'grey\' or color = \'black\' or color = \'blue\' order by rand() limit 2'
    elif(color=='beige'):
        return 'color=\'brown\' or color = \'black\' or color = \'white\' order by rand() limit 2'
    elif(color=='ivory'):
        return 'color=\'ivory\' or color = \'black\' or color = \'white\' order by rand() limit 2'    
    #data=data.form['data']
    # imgdata = base64.b64decode(data)
    # dataBytesIO = io.BytesIO(imgdata)
    # image = Image.open(dataBytesIO)
    # return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    
if __name__ == '__main__':
    #print(testFunc(sys.argv[1]))
    print(testFunc(sys.argv[1]))
    #print(testFunc())