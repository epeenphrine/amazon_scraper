from amazon_scrape import amazon_scrape
from ebay_scrape import ebay_scrape
from baba_scrape import baba_scrape
from walmart_scrape import walmart_scrape

def working(search):

    ebay = ebay_scrape(search)
    amazon = amazon_scrape(search)
    baba = baba_scrape(search)
    walmart = walmart_scrape(search)