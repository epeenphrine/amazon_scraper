
import urllib.request
import bs4 as bs
import json
import random
import os
import time
from config import search 
from proxy_rotate import proxy_rotate

"""
goal is to be able to dynamically search amazon and get prices for various items using scraping techniques
"""


def amazon_scrape():
    #search and url
    url = f"https://www.amazon.com/s?k={search}&ref=nb_sb_noss_2"

    #pass soup from proxyrotate
    soup = proxy_rotate(url)

    ## check html
    amazon = {

    }
    titles = []
    listings = []
    for title  in soup.select('.a-size-medium.a-text-normal'):
        titles.append(title.get_text(strip=True))
    amazon['item_name'] = titles

    for listing  in soup.select('.s-latency-cf-section'):
        listings.append(listing.get_text(strip=True))
    amazon['listing'] = listings

    items = []
    def test():
        for item in soup.select('.sg-col-20-of-28 .sg-col-inner'):
            text = item.get_text(strip=True).lower()
            if "$" in text and 'sponsored' not in text and all(word in text for word in config.split_search):
                items.append(text)
    amazon['items'] = items
    return amazon

    #print(len(amazon['item_name']))

    #print(len(amazon['listing']))

    test()

    #print(amazon['items'])
    #print(len(amazon['items']))
