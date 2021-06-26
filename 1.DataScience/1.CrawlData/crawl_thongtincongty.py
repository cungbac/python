# Packages to crawl website
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import randint
import csv

# Packages to save png images
import base64
from PIL import Image
from io import BytesIO

# Packages to read png images into text
import pytesseract

def crawl_company_info():
    """This is to scrap company information from thongtincongty.com"""
    # open browser
    driver = webdriver.Chrome('chromedriver')

    # set time sleep
    time_sleep = randint(1,3)

    # open csv file
    with open('thongtincongty.csv', mode= 'w', newline='') as file:
        headers = ['No','Company Name','Registration Number', 'Representative', 'Street', 'Ward','District','Province','Link']
        writer = csv.writer(file)
        writer.writerow(headers)

    # folder to save png image
    path = '/Users/bactran/Documents/1.Learning/2.Python/1.DataScience/1.CrawData/image_MST'

    # input number of pages 
    pages = int(input('How many pages you want to scrap: '))

    # Get data
    index = 0
    for page in range(1,pages + 1):
        # link
        pre_link = 'https://www.thongtincongty.com/?page='
        link = pre_link + str(page)

        driver.get(link)
        sleep(time_sleep)

        # get info
        page_source = driver.page_source
        soup = BeautifulSoup(page_source,'html.parser')

        all_info = soup.find_all('div',{'class':'search-results'})

        img_links = soup.findAll('img')
        links = []
        mst_list = []
        # info in text
        for i in range(len(all_info)):
            # title
            title = all_info[i].find('a').get_text()
            
            # link
            link = all_info[i].find('a', href = True)
            link = link.get('href')
            
            # representative & address
            info_text = all_info[i].get_text()
            
            # representative 
            representative = info_text[info_text.find('- Đại diện pháp luật:') + len('- Đại diện pháp luật:'): info_text.find('Địa chỉ:')].strip()
            
            # address
            address = info_text[info_text.find('Địa chỉ:') + len('Địa chỉ:'):].strip()
            address = address.split(',')

            province = address[- 1].strip()
            district = address[- 2].strip()
            ward = address[- 3].strip()
            street_list = address[:- 3]
            street = ''.join(str(i) for i in street_list).strip()

            # find all img base64 code
            src = img_links[i].get('src')
            if src.find('data:image/png;base64,') >= 0:
                src = src[len('data:image/png;base64,'):].strip()
                links.append(src)

            # save MST as png file in the folder
            img = Image.open(BytesIO(base64.b64decode(links[i])))
            img_path = path + '/img_page' + str(page) + '_' + str(i) + '.png'
            img.save(img_path, 'PNG')

            # read base64 image to text
            img_open = Image.open(img_path)
            img_text = pytesseract.image_to_string(img_open,config='--psm 10').strip()

            # add to data
            index += 1
            data = [index, title, img_text, representative, street, ward, district, province, link]

            # write into csv file
            with open('thongtincongty.csv', mode='a',newline='') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerow(data)

        sleep(time_sleep)
    
    # Quit
    sleep(time_sleep)
    driver.quit()

# RUN
crawl_company_info()