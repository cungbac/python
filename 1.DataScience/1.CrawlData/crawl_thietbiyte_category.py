# import packages
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import csv
from time import sleep
from random import randint

# time sleep
timesleep = randint(1, 3)

# url
url = 'https://congkhaigiadmec.moh.gov.vn/tra-cuu-nhom'

# driver
driver = webdriver.Chrome('chromedriver_win')
driver.get(url)

sleep(2)

div = driver.find_elements_by_tag_name('li')

with open('thietbiyte.csv',mode='w',encoding='utf8',newline='') as file:
    headers = ['Group1','Group2','Group3','Group4']
    writer = csv.writer(file)
    writer.writerow(headers)

# item_menu = driver.find_elements_by_class_name('item-menu__text')

soup = BeautifulSoup(driver.page_source,'html.parser')


print('---sub menu---')
sleep(timesleep)

xpath_pre = '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div['
xpath_suf = ']/div[1]/div/h3'

css_selectors_item_menu_pre = '#root > div > div.app > div > div > div.container.container-inner > div > div > div:nth-child('
css_selectors_item_menu_mid = ') > div.booth-body-title > div > nav > ul > li:nth-child('
css_selectors_item_menu_suf = ') > div'


css_selectors_sub_item_menu_pre = '#root > div > div.app > div > div > div.container.container-inner > div > div > div:nth-child('
css_selectors_sub_item_menu_mid_1 = ') > div.booth-body-title > div > nav > ul > li:nth-child('
css_selectors_sub_item_menu_mid_2 = ') > ul > li:nth-child('
css_selectors_sub_item_menu_suf = ')'


'#root > div > div.app > div > div > div.container.container-inner > div > div > div:nth-child(1) > div.booth-body-title > div > nav > ul > li:nth-child(4) > div'

item_count = 0
item_menu_count = 0

sleep(timesleep)
thietbiyte = []
for xpath in range(1,4):
    xpath_item = xpath_pre + str(xpath) + xpath_suf
    driver.find_element_by_xpath(xpath_item).click()

    item_menu = soup.find_all('div',{'class':'item-menu__text'})

    print(xpath,'---item menu---')
    print('len item menu: ',len(item_menu))
    for item in item_menu:
        print(item.get_text())
    sleep(timesleep)
    
    for i in range(1,len(item_menu) + 1):
        css_selectors_item = css_selectors_item_menu_pre + str(xpath) + css_selectors_item_menu_mid + str(i) + css_selectors_item_menu_suf

        item_to_hover = driver.find_element_by_css_selector(css_selectors_item)
        sleep(timesleep)

        hover_item = ActionChains(driver).move_to_element(item_to_hover)
        sleep(timesleep)

        hover_item.perform()
        sleep(timesleep)

        sub_item_menus = BeautifulSoup(driver.page_source,'html.parser').find_all('li',{'class':'sub-item-menu'})
        
        print(i,'---sub item menu---')
        print('len sub item menus',len(sub_item_menus))
        print('item count',item_count)
        print('check len sub',len(sub_item_menus) - item_count + 1)

        count_1 = len(sub_item_menus)

        for item in sub_item_menus:
            print(item.get_text())
        sleep(timesleep)
        
        for j in range(1,len(sub_item_menus) - item_count + 1):
            print('css_1',xpath)
            print('css_2',i)
            print('css_3',j)
            print('---')

            css_selectors_sub_item = css_selectors_sub_item_menu_pre + str(xpath) + css_selectors_sub_item_menu_mid_1 + str(i) + css_selectors_sub_item_menu_mid_2 + str(j) + css_selectors_sub_item_menu_suf

            sub_item_to_hover = driver.find_element_by_css_selector(css_selectors_sub_item)
            sleep(timesleep)
            
            hover_sub_item = ActionChains(driver).move_to_element(sub_item_to_hover)
            sleep(timesleep)

            hover_sub_item.perform()
            sleep(timesleep)
            
            sub2_item_menus = BeautifulSoup(driver.page_source,'html.parser').find_all('li',{'class':'sub2-item-menu'})

            for item in sub2_item_menus:
                group1 = 'Thiet bi y te'.strip()
                group2 = item_menu[i-1-item_menu_count].get_text().strip()
                group3 = sub_item_menus[j-1+item_count].get_text().strip()
                group4 = item.get_text().strip()
                data = [group1,group2,group3,group4]
                
                with open('thietbiyte.csv',mode='a',encoding='utf8',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
                # print(item.get_text())
                sleep(timesleep)
            sleep(timesleep)
        sleep(timesleep)
        item_count = len(sub_item_menus)

    count_2 = len(sub2_item_menus)
    item_menu_count += count_2
    print(item_menu_count)
    sleep(timesleep)

sleep(timesleep)
driver.quit()
