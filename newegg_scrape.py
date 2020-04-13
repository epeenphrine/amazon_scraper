
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
goal is to be able to dynamically search newegg and get prices for various items using scraping techniques
"""


def newegg_scrape(search):
    print(f'searching newegg for {search} ')
    split_search = search.split(" ")
    search = search.replace(" ", "+")
    base_url = 'https://newegg.com'

    #search and url
    url = f"https://www.newegg.com/p/pl?d={search}"

    #pass soup from proxyrotate
    soup = proxy_rotate(url)

    newegg = {

    }

    items = []
    prices = []
    numbers = []
    links = []
    for item in soup.findAll('div',{'class':'item-container'}):
        text = item.get_text(strip=True).lower()
        if "$" in text:
            # get first match of regular expression
            price = re.search("\$\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
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
                numbers.append(float(price.replace('$', '').replace(',', '')))
    
    average = ("{:.2f}").format(statistics.mean(numbers))
    
    newegg['id'] = 4
    newegg['ecommerce'] = 'newegg'
    newegg['items'] = items
    newegg['links'] = links
    newegg['prices'] = prices
    newegg['numbers'] = numbers 
    newegg['average'] = average

    ## checck
    #print(newegg['id'])
    #print(newegg['ecommerce'])
    #print(newegg['items'])
    #print(newegg['prices'])
    #print(newegg['numbers'])
    #print(newegg['average'])

    return newegg
