import json


res= [
    {"id":2,"ticker":"spy","x":"[1]","y":"[2]","owner":1}, ## amazon 
    {"id":3,"ticker":"spy","x":"[5]","y":"[3]","owner":1}, ## ebay
    {"id":4,"ticker":"googl","x":"[1,2,3,4,5,6]","y":"[7,8,9,10,11]","owner":1} ## baba 
    ## etc etc 
    ]

together = []

amazon ={
    'id': '1',
    'ecommerce': 'amazon',
    'items': 'item',
    'prices': 'item_prices', ## need to scrape
    'avg_price': 'number', ## use scraped data 
    'URLs': 'url' ## need to scrape

}

baba ={
    'id': '2',
    'ecommerce': 'baba',
    'items': 'item',
    'prices': 'item_prices',
    'avg_price': 'number',
    'URLs': 'url'

}

together.append(amazon)
together.append(baba)

print(together)