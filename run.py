from amazon_scrape import amazon_scrape
from ebay_scrape import ebay_scrape
from baba_scrape import baba_scrape
from walmart_scrape import walmart_scrape
from newegg_scrape import newegg_scrape


def scrape(search):
    ecommerces = [

    ]
    try: 
        ebay = ebay_scrape(search)
    except: 
        print("couldn't get ebay")
        ebay = None
    try:
        amazon = amazon_scrape(search)
    except:
        print("couldn't get amazon")
        amazon = None
    try:
        baba = baba_scrape(search)
    except:
        print("coudln't get baba")
        baba= None
    try:
        walmart = walmart_scrape(search)
    except:
        print("couldn't get walmart")
        walmart= None
    try:
        newegg = newegg_scrape(search)
    except:
        print("couldn't get newegg")
        newegg = None

    if amazon != None:
        print('amazon : ')
        print(amazon['prices'])
        print(amazon['average'])
        ecommerces.append(amazon)
    if baba != None:
        print('baba : ')
        print(baba['prices'])
        print(baba['average'])
        ecommerces.append(baba)
    if walmart != None:
        print('walmart : ')
        print(walmart['prices'])
        print(walmart['average'])
        ecommerces.append(walmart)
    if ebay !=None:
        print('ebay : ')
        print(ebay['prices'])
        print(ebay['average'])
        ecommerces.append(ebay)
    if newegg != None:
        print('newegg : ')
        print(newegg['prices'])
        print(newegg['average'])
        ecommerces.append(newegg)
    
    return ecommerces