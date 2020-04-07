
import urllib.request
import bs4 as bs
import json
import random
import os
import time
import config

"""
goal is to be able to dynamically search amazon and get prices for various items using scraping techniques
"""

#search and url
search = config.search
url = f"https://www.amazon.com/s?k={search}&ref=nb_sb_noss_2"

#making requests using urllib

req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})

sauce = urllib.request.urlopen(req, timeout=5).read()

code = urllib.request.urlopen(req, timeout=5).getcode()


## check https code
if code == 200:
    print(f'connection success, http code : {code}')
    soup = bs.BeautifulSoup(sauce, 'lxml')
else:
    print(f'ran into error, http code : {code}')

print(soup)