import urllib.request
import bs4 as bs
import json
import random
import os
import time
from proxy_rotate import proxy_rotate
import re
import statistics

"""
goal is to be able to dynamically search baba and get prices for various items using scraping techniques
"""


def baba_scrape(search):
    print(f'searching baba for {search} ')
    split_search = search.split(" ")
    search = search.replace(" ", "+")
    base_url = 'https://alibaba.com'

    #search and url
    url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search}"

    #pass soup from proxyrotate
    soup = proxy_rotate(url)

    baba = {

    }

    items = []
    prices = []
    numbers = []
    links = []

    for item in soup.select('.img-switcher-parent'):
        text = item.get_text(strip=True).lower()
        #if "$" in text:
        if "$" in text and all(word in text for word in split_search):
            # get first match of regular expression
            price = re.search("\$\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d,\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
            no_price = re.search('$0.00',text)
            if price != None and no_price == None:
                # bs4 .find match first a tag 
                a = item.find('a', href=True)
                link = base_url + a['href']
                links.append(link)
                # .group() to convert regex object into string. price != None so that we don't run into error  
                price = price.group()
                items.append(text)
                prices.append(price)
                #numbers.append(float(price.replace('$', '')))
                numbers.append(float(price.replace('$', '').replace(',', '')))
    
    average = ("{:.2f}").format(statistics.mean(numbers))
    
    baba['id'] = 2
    baba['ecommerce'] = 'baba'
    baba['items'] = items
    baba['links'] = links
    baba['prices'] = prices
    baba['numbers'] = numbers 
    baba['average'] = average

    ## checck
    #print(baba['id'])
    #print(baba['ecommerce'])
    #print(baba['items'])
    #print(baba['prices'])
    #print(baba['numbers'])
    #print(baba['average'])

    return baba

