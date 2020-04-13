
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
goal is to be able to dynamically search amazon and get prices for various items using scraping techniques
"""


def amazon_scrape(search):
    print(f'searching amazon for {search} ')
    split_search = search.split(" ")
    search = search.replace(" ", "+")
    base_url = 'https://amazon.com'

    #search and url
    url = f"https://www.amazon.com/s?k={search}&ref=nb_sb_noss_2"

    #pass soup from proxyrotate
    soup = proxy_rotate(url)

    amazon = {

    }

    items = []
    prices = []
    numbers = []
    links = []

    for item in soup.select('.sg-col-20-of-28 .sg-col-inner'):
        text = item.get_text(strip=True).lower()
        if "$" in text and 'sponsored' not in text and all(word in text for word in split_search):
            # get first match of regular expression
            price = re.search("\$\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
            if price != None:
                # bs4 .find match first a tag 
                a = item.find('a', href=True)
                link = base_url + a['href']
                links.append(link)
                # .group() to convert regex object into string. price != None so that we don't run into error  
                price = price.group()
                items.append(text)
                prices.append(price)
                numbers.append(float(price.replace('$', '')))
    
    average = ("{:.2f}").format(statistics.mean(numbers))
    
    amazon['id'] = 1
    amazon['ecommerce'] = 'amazon'
    amazon['items'] = items
    amazon['links'] = links
    amazon['prices'] = prices
    amazon['numbers'] = numbers 
    amazon['average'] = average

    ## checck
    #print(amazon['id'])
    #print(amazon['ecommerce'])
    #print(amazon['items'])
    #print(amazon['prices'])
    #print(amazon['numbers'])
    #print(amazon['average'])

    return amazon
