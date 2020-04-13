

import urllib.request
import bs4 as bs
import json
import random
import os
import time
import config 
from proxy_rotate import proxy_rotate
import re
import statistics

"""
goal is to be able to dynamically search ebay and get prices for various items using scraping techniques
"""

def ebay_scrape(search):
    print(f'searching ebay for {search} ')
    split_search = search.split(" ")
    search = search.replace(" ", "+")
    base_url = 'https://ebay.com'

    #search and url
    #url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR5.TRC2.A0.H0.X{search}.TRS0&_nkw={search}&_sacat=0"
    url =  f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={search}0&_sacat=0&rt=nc&LH_BIN=1" 
    #pass soup from proxyrotate
    soup = proxy_rotate(url)

    ebay = {

    }

    items = []
    prices = []
    numbers = []
    links = []
    for item in soup.select('.s-item'):
        text = item.get_text(strip=True).lower()
        if "$" in text and all(word in text for word in split_search):
            # get first match of regular expression
            price = re.search("\$\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d,\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
            no_price = re.search('$0.00',text)
            if price != None and no_price == None:
                # bs4 .find match first a tag 
                a = item.find('a', href=True)
                link = a['href']
                links.append(link)
                # .group() to convert regex object into string. price != None so that we don't run into error  
                price = price.group()
                items.append(text)
                prices.append(price)
                numbers.append(float(price.replace('$', '').replace(',', '')))
    
    average = ("{:.2f}").format(statistics.mean(numbers))
    
    ebay['id'] = 3
    ebay['ecommerce'] = 'ebay'
    ebay['items'] = items
    ebay['links'] = links
    ebay['prices'] = prices
    ebay['numbers'] = numbers 
    ebay['average'] = average

    ## checck
    #print(ebay['id'])
    #print(ebay['ecommerce'])
    #print(ebay['items'])
    #print(ebay['prices'])
    #print(ebay['numbers'])
    #print(ebay['average'])

    return ebay

