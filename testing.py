from amazon_scrape import amazon_scrape
from ebay_scrape import ebay_scrape
from baba_scrape import baba_scrape
from walmart_scrape import walmart_scrape
search = "nvidia gtx 1080"
def working(search):

    ebay = ebay_scrape(search)
    amazon = amazon_scrape(search)
    baba = baba_scrape(search)
    walmart = walmart_scrape(search)

    print(amazon['prices'])
    print(ebay['prices'])
    print(baba['prices'])
    print(walmart['prices'])

    print(amazon['average'])
    print(ebay['average'])
    print(baba['average'])
    print(walmart['average'])


def test(search):
    walmart_scrape(search)
    pass


test(search)