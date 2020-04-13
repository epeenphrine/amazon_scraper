import urllib.request
import bs4 as bs
import json
import random
import os
import time
from proxy_rotate import proxy_rotate
import re
import statistics
import time 
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
    findings = soup.findAll('script')
    finding = findings[20]
    findingg = finding.contents[0]
    json_dataa = json.loads(findingg)
    ##debugging
    #position = 0 
    #for item in findings:
        #print(f'this is position : {position}')
        #print(item)
        #position += 1
    
    data = soup.find("script", {"id": "searchContent"})
    data = data.contents[0].string
    json_data = json.loads(data)
    try:
        for item in json_data['searchContent']['preso']['items']:
            items.append(item['title'])
            links.append(item['productPageUrl'])
            prices.append('$'+str(item['primaryOffer']['offerPrice']))
            numbers.append(item['primaryOffer']['offerPrice'])
    except:
        print('not a good web page... breaking')

    
    
    #for item in soup.findAll('li',{'id':'ProductTileGridView'}):
        #text = item.get_text(strip=True).lower()
        #if "$" in text:
            ## get first match of regular expression
            #price = re.search("\$\d\d\d.\d\d|\$\d\d\d\d.\d\d|\$\d\d\.\d\d|\$\d\.\d\d", text)
            #no_price = re.search('$0.00',text)
            #if price != None and no_price == None:
                ## bs4 .find match first a tag 
                #a = item.find('a', href=True)
                #link = base_url + a['href']
                #links.append(link)
                ## .group() to convert regex object into string. price != None so that we don't run into error  
                #price = price.group()
                #items.append(text)
                #prices.append(price)
                #numbers.append(float(price.replace('$', '').replace(',', '')))
    

    average = ("{:.2f}").format(statistics.mean(numbers))
    
    walmart['id'] = 5
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

