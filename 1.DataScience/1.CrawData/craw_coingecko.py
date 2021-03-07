# Import packages
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import csv
import datetime

# Write functions

# Get index of a second repeated character
def get_index(input_string,character,ordinal):
    """get index of a repeated character in the string"""
    current = 0
    for i in range(ordinal):
        current = input_string.index(character,current + 1)
    return current

# Replace multiple characters
def replace_charactors(a_string, text_1, text_2):
    a_string = a_string.replace(text_1,'')
    a_string = a_string.replace(text_2,'')
    return a_string

# Get links of coins
def get_links(numbers,driver):
    page_source = BeautifulSoup(driver.page_source,features='html.parser')
    coin_links = page_source.findAll('a',{'class':'d-lg-none font-bold'})

    all_link = []
    for i in range(numbers):
        pre_href = 'https://www.coingecko.com'
        suf_href = coin_links[i].get('href')
        coin_link = pre_href + suf_href
        all_link.append(coin_link)
    return all_link

# Get coin info
def get_coin_info(numbers,driver):
    all_link = get_links(numbers=numbers,driver=driver)
    time_sleep = randint(1,3)
    current = datetime.datetime.now()

    for i in range(numbers):
        driver.get(all_link[i])

        page_source = BeautifulSoup(driver.page_source,features='html.parser')
        
        # coin name
        coin_name = page_source.find('h1',{'class':'mr-md-3 mx-2 mb-md-0 text-3xl font-semibold'})
        coin_name = coin_name.get_text().strip()

        name = coin_name[:coin_name.find('(')].strip()
        symbol = coin_name[coin_name.find('(')+1:coin_name.find(')')].strip()

        # general info
        general_info = page_source.find('div',{'class':'mt-1 mb-3 d-flex flex-wrap'})
        general_info = general_info.get_text().strip()

        # market cap
        market_cap = general_info[general_info.find('Market Cap') + len('Market Cap') : general_info.find('24 Hour Trading Vol')].strip()
        market_cap = market_cap.replace('$','')
        market_cap = float(replace_charactors(market_cap,'$',','))

        # volume_24h
        volume_24h_usd = general_info[general_info.find('24 Hour Trading Vol') + len('24 Hour Trading Vol'):general_info.find('24h Low / 24h High')].strip()
        volume_24h_usd = float(replace_charactors(volume_24h_usd,'$',','))

        # low high 24h
        low_high_24h = general_info[general_info.find('24h Low / 24h High') + len('24h Low / 24h High'):general_info.find('Circulating Supply')]
        
        low_24h_usd = low_high_24h[:low_high_24h.find('/')].strip()
        low_24h_usd = float(replace_charactors(low_24h_usd,'$',','))

        high_24h_usd = low_high_24h[low_high_24h.find('/') + 1:].strip()
        high_24h_usd = float(replace_charactors(high_24h_usd,'$',','))

        # circulating & total supply
        try:
            circulating_fraction = general_info[general_info.find('Circulating Supply') + len('Circulating Supply'):general_info.find('Fully Diluted Valuation')].strip()
        except:
            circulating_fraction = general_info[general_info.find('Circulating Supply') + len('Circulating Supply'):].strip()

        circulating_supply = circulating_fraction[:circulating_fraction.find('/')].strip()

        total_supply = circulating_fraction[circulating_fraction.find('/')+1:].strip()
        total_supply = total_supply.replace(',','')

        # Price
        price_change_info = page_source.find('div',{'class':'col-lg-5 col-md-5 text-center text-md-right mt-md-0 pr-0'})
        price_change_info = price_change_info.get_text().strip()

        price_usd = price_change_info[:price_change_info.find('\n')].strip()
        price_usd = float(replace_charactors(price_usd,'$',','))

        change_usd = price_change_info[price_change_info.find('\n'):price_change_info.find('%')+1].strip()
        change_usd = float(change_usd.replace('%',''))/100

        price_btc = price_change_info[price_change_info.find('%')+1:price_change_info.find('BTC')].strip()

        change_btc = price_change_info[price_change_info.find('BTC') + 3: get_index(price_change_info,'%',2) + 1].strip()
        change_btc = float(change_btc.replace('%',''))/100

        try:
            price_eth = price_change_info[get_index(price_change_info,'%',2): price_change_info.index('ETH',0)].strip()

            change_eth = price_change_info[price_change_info.index('ETD',0)+3:].strip()
            change_eth = float(change_eth.replace('%',''))/100

        except:
            price_eth = ''
            change_eth = ''

        # Check the second info is Market Cap or ROI
        second_info = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/th')
        second_info = second_info.text.strip()

        # ROI
        if second_info.find('ROI') > 0:
            ROI = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td/span')
            ROI = ROI.text.strip()
            ROI = float(ROI.replace('%',''))/100

        else:
            ROI = ''

        # Market Cap Dominance
        if second_info.find('ROI') > 0:
            market_cap_dominance = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[4]/td')
            market_cap_dominance = market_cap_dominance.text.strip()
            market_cap_dominance = float(market_cap_dominance.replace('%',''))/100
        else:
            market_cap_dominance = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[3]/td')
            market_cap_dominance = market_cap_dominance.text.strip()
            market_cap_dominance = float(market_cap_dominance.replace('%',''))/100

        # Low 7 days
        if second_info.find('ROI') > 0:
            low_7day_usd = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[8]/td/span[1]')
            low_7day_usd = low_7day_usd.text.strip()
            low_7day_usd = float(replace_charactors(low_7day_usd,'$',','))
        else:
            low_7day_usd = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[7]/td/span[1]')
            low_7day_usd = low_7day_usd.text.strip()
            low_7day_usd = float(replace_charactors(low_7day_usd,'$',','))

        # High 7 days
        if second_info.find('ROI') > 0:
            high_7day_usd = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[8]/td/span[2]')
            high_7day_usd = high_7day_usd.text.strip()
            high_7day_usd = float(replace_charactors(high_7day_usd,'$',','))
        else:
            high_7day_usd = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[7]/td/span[2]')
            high_7day_usd = high_7day_usd.text.strip()
            high_7day_usd = float(replace_charactors(high_7day_usd,'$',','))

        # Market Cap Rank
        if second_info.find('ROI') > 0:
            market_cap_rank = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[9]/td')
            market_cap_rank = market_cap_rank.text.strip()
            market_cap_rank = int(market_cap_rank.replace('#',''))
        else:
            market_cap_rank = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[8]/td')
            market_cap_rank = market_cap_rank.text.strip()
            market_cap_rank = int(market_cap_rank.replace('#',''))

        # All time high value
        try:
            all_time_high_price = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[9]/td/span[1]')
            all_time_high_price = all_time_high_price.text.strip()
            all_time_high_price = float(replace_charactors(all_time_high_price,'$',','))
        except:
            all_time_high_price = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[10]/td/span[1]')
            all_time_high_price = all_time_high_price.text.strip()
            all_time_high_price = float(replace_charactors(all_time_high_price,'$',','))
        
        # All time high time
        try:
            all_time_high_time = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[9]/td/small')
            all_time_high_time = all_time_high_time.text.strip()
            all_time_high_time = all_time_high_time[:all_time_high_time.find('(')]
        except:
            all_time_high_time = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[10]/td/small')
            all_time_high_time = all_time_high_time.text.strip()
            all_time_high_time = all_time_high_time[:all_time_high_time.find('(')]

        # All time low value
        try:
            all_time_low_price = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[10]/td/span[1]')
            all_time_low_price = all_time_low_price.text.strip()
            all_time_low_price = float(replace_charactors(all_time_low_price,'$',','))
        except:
            all_time_low_price = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[11]/td/span[1]')
            all_time_low_price = all_time_low_price.text.strip()
            all_time_low_price = float(replace_charactors(all_time_low_price,'$',','))

        # All time low time
        try:
            all_time_low_time = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[10]/td/small')
            all_time_low_time = all_time_low_time.text.strip()
            all_time_low_time = all_time_low_time[:all_time_low_time.find('(')]
        except:
            all_time_low_time = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[2]/div[1]/div/table/tbody/tr[11]/td/small')
            all_time_low_time = all_time_low_time.text.strip()
            all_time_low_time = all_time_low_time[:all_time_low_time.find('(')]

        # Growth 1 hour
        try:
            growth_1h = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[1]/div/div[2]/div[2]/div[1]/span')
            growth_1h = growth_1h.text.strip()
            growth_1h = float(growth_1h.replace('%',''))/100
        except:
            growth_1h = None

        # Growth 24 hours
        try:
            growth_24h = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[1]/div/div[2]/div[2]/div[2]/span')
            growth_24h = growth_24h.text.strip()
            growth_24h = float(growth_24h.replace('%',''))/100
        except:
            growth_24h = None

        # Growth 7 days
        try:
            growth_7d = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[1]/div/div[2]/div[2]/div[3]/span')
            growth_7d = growth_7d.text.strip()
            growth_7d = float(growth_7d.replace('%',''))/100
        except:
            growth_7d = None

        # Growth 14 days
        try:
            growth_14d = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[1]/div/div[2]/div[2]/div[4]/span')
            growth_14d = growth_14d.text.strip()
            growth_14d = float(growth_14d.replace('%',''))/100
        except:
            growth_14d = None

        # Growth 30 days
        try:
            growth_30d = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[1]/div/div[2]/div[2]/div[5]/span')
            growth_30d = growth_30d.text.strip()
            growth_30d = float(growth_30d.replace('%',''))/100
        except:
            growth_30d = None

        # Growth 1 year
        try:
            growth_1y = driver.find_element_by_xpath('//*[@id="general"]/div[1]/div[1]/div/div[2]/div[2]/div[6]/span')
            growth_1y = growth_1y.text.strip()
            growth_1y = float(growth_1y.replace('%',''))/100
        except:
            growth_1y = None

        data = [name, symbol, price_usd, change_usd, price_btc, change_btc, ROI, market_cap, volume_24h_usd, low_24h_usd, high_24h_usd, circulating_supply, total_supply, market_cap_dominance, low_7day_usd, high_7day_usd, market_cap_rank, all_time_high_price, all_time_high_time, all_time_low_price, all_time_low_time, growth_1h, growth_24h, growth_7d, growth_14d, growth_30d, growth_1y, current]

        with open('coin_list.csv', mode= 'a', newline= '') as file_csv:
            writer = csv.writer(file_csv)
            writer = writer.writerow(data)

        sleep(time_sleep)
    
# Run
time_sleep = randint(1,3)

# Open browser
driver = webdriver.Chrome('chromedriver')
link = 'https://www.coingecko.com/en'

driver.get(link)

numbers = int(input('How many coins: '))

# with open('coin_list.csv', mode='w', newline= '') as file:
#     headers = ['Name', 'Symbol','Price (USD)','Percent change (USD)','Price (BTC)','Percent change (BTC)', 'ROI','Market Cap', 'Volume in 24h', 'Low in 24h', 'High in 24h','Circulating Supply', 'Total Supply','Market Cap Dominance', 'Low in 7 days','High in 7 days','Market Cap Rank', 'All Time High', 'All Time High - time', 'All Time Low', 'All Time Low - time', 'Growth 1h', 'Growth 24h', 'Growth 7d', 'Growth 14d', 'Growth 30d', 'Growth 1y','Lastest refreshed']
#     writer = csv.writer(file)
#     writer = writer.writerow(headers)

# Get info
get_coin_info(numbers,driver)

# Quit browser
sleep(time_sleep)

driver.quit()
