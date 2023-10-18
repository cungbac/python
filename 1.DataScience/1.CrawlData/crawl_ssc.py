# test edit from github ui
# import packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import pandas as pd


# driver 
driver = webdriver.Chrome('chromedriver_win')
link_ssc = 'http://www.ssc.gov.vn/ubck/faces/vi/vimenu/vipages_vicsdlcty/ctychungkhoan?_adf.ctrl-state=tu0ft6b50_4&_afrLoop=16628340649000'

driver.get(link_ssc)

# parse page source
page_source = driver.page_source
soup = BeautifulSoup(page_source,'html.parser')

# td = page_source.find_all('tr')

td = driver.find_elements_by_tag_name('tr')

text_list = [i.text for i in td]
print(text_list)

sleep(5)
driver.quit()
