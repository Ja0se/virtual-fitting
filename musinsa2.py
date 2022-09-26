import re
import time
import base64
import requests
import numpy as np
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

check = False

options = Options()
# options.add_argument()

url = 'https://www.musinsa.com/mz/brandsnap'
# s = Service('./chromedriver.exe')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url)

totalPage = driver.find_element(By.CLASS_NAME, 'totalPagingNum').text
totalPage = re.findall('\d+', totalPage)
totalPage = int(''.join(totalPage))

totalImg = []

for item in range(totalPage//10-1):
    pageBox = driver.find_elements(By.CSS_SELECTOR, '.pagination > div > a')
    for idx in range(2, 12):
        pageBox[idx].send_keys('\n')
        time.sleep(1)
        imgList = driver.find_elements(By.CSS_SELECTOR, '.articleImg > a > img')
        
        for img in imgList:
            #totalImg.append(base64.b64encode(requests.get(img.get_attribute('src')).content))
            # totalImg.append(img.get_attribute('src'))
            res = requests.get(img.get_attribute('src'))
            img = Image.open(BytesIO(res.content))
            npimg = np.array(img)
            print(npimg)
            
        pageBox = driver.find_elements(By.CSS_SELECTOR, '.pagination > div > a')
    pageBox[12].send_keys('\n')
    time.sleep(1)

driver.quit()
