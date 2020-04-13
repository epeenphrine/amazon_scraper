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
goal is to be able to dynamically search walmart and get prices for various items using scraping techniques
"""


def walmart_scrape(search):
    print(f'searching walmart for {search} ')
    split_search = search.split(" ")
    search = search.replace(" ", "%20")
    base_url = 'https://walmart.com'

    #search and url
    url = f"https://www.walmart.com/search/?query={search}"

    #pass soup from proxyrotate
    soup = proxy_rotate(url)

    walmart = {

    }

    items = []
    prices = []
    numbers = []
    links = []
    ## convert type: application/json soup object into string then json 
    data = soup.find("script", {"id": "searchContent"})
    
    data = data.contents[0].string
    json_data = json.loads(data.string)
    print(type(json_data))

    for item in json_data['searchContent']['preso']['items']:
        print(item['primaryOffer']['offerPrice'])
        break
    
    #for item in soup.select('.u-size-1-5-xl'):
    for item in soup.select('Grid'):
        text = item.get_text(strip=True).lower()
        print(text)
        if "$" in text and 'sponsored' not in text and all(word in text for word in split_search):
            # get first match of regular expression
            price = re.search("\$\d\d\d.\d\d|\$\d,\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
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
    
    walmart['id'] = 1
    walmart['ecommerce'] = 'walmart'
    walmart['items'] = items
    walmart['links'] = links
    walmart['prices'] = prices
    walmart['numbers'] = numbers 
    walmart['average'] = average

    # checck
    #print(walmart['id'])
    #print(walmart['ecommerce'])
    #print(walmart['items'])
    #print(walmart['prices'])
    #print(walmart['numbers'])
    #print(walmart['average'])

    return walmart

