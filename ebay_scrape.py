

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
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR5.TRC2.A0.H0.X{search}.TRS0&_nkw={search}&_sacat=0"

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
        if "$" in text and 'sponsored' not in text and all(word in text for word in split_search):
            # get first match of regular expression
            price = re.search("\$\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
            if price != None:
                # bs4 .find match first a tag 
                a = item.find('a', href=True)
                link = a['href']
                links.append(link)
                # .group() to convert regex object into string. price != None so that we don't run into error  
                price = price.group()
                items.append(text)
                prices.append(price)
                numbers.append(float(price.replace('$', '')))
    
    average = ("{:.2f}").format(statistics.mean(numbers))
    
    ebay['id'] = 1
    ebay['ecommerce'] = 'ebay'
    ebay['items'] = items
    ebay['links'] = links
    ebay['prices'] = prices
    ebay['numbers'] = numbers 
    ebay['average'] = average

    print(ebay['links'])
    print(ebay['prices'])
    print(ebay['average'])

    ## checck
    #print(ebay['id'])
    #print(ebay['ecommerce'])
    #print(ebay['items'])
    #print(ebay['prices'])
    #print(ebay['numbers'])
    #print(ebay['average'])

    return ebay

