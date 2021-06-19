from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import os
import pandas 
chromeDriver = os.path.expanduser('~\\Documents\\chromedriver_win32\\chromedriver.exe')
url = "https://dichvucong.dav.gov.vn/congbogiathuoc/index"
driver = webdriver.Chrome(chromeDriver)
driver.get(url)

# go to next page
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
output=[]
i = 0
while i < 3914:
    page_html_source = driver.page_source
    page_soup = BeautifulSoup(page_html_source, 'html.parser')
    td = page_soup.find_all('tr')
    for t in td:
        list = [r.get_text() for r in t]
        print(list)
        output.append(list)
    driver.find_element_by_xpath("//*[@id='gridGiaThuoc']/div[3]/a[3]").click()
    i += 1
driver.close()
df_duoc = pandas.DataFrame(output)
df_duoc.to_excel (r'C:\DATA PROCESSING_REPORTING\data.xlsx', index = False, header=True)

