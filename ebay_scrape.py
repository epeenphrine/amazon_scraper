

import urllib.request
import bs4 as bs
import json
import random
import os
import time
import config 
from proxy_rotate import proxy_rotate

"""
goal is to be able to dynamically search amazon and get prices for various items using scraping techniques
"""

def ebay_scrape():

    #search and url
    search = config.search
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xrtx+2080.TRS0&_nkw=rtx+2080&_sacat=0"

    #making requests using urllib

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
        for item in soup.select('.s-item'):
            text = item.get_text(strip=True).lower()
            if "$" in text and 'sponsored' not in text and all(word in text for word in config.split_search):
                items.append(text)
    amazon['items'] = items


    #print(len(amazon['item_name']))

    #print(len(amazon['listing']))

    test()
    #print(amazon['items'])
    #print(len(amazon['items']))