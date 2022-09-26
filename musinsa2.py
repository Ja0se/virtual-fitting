import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

check = False

options = Options()
# options.add_argument()

url = 'https://www.musinsa.com/mz/brandsnap'
s = Service('./chromedriver')
driver = webdriver.Chrome(service = s, options=options)
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
            totalImg.append(img.get_attribute('src'))
            print(totalImg)
       
        pageBox = driver.find_elements(By.CSS_SELECTOR, '.pagination > div > a')
    pageBox[12].send_keys('\n')
    time.sleep(1)

driver.quit()