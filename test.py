import requests
#url = 'http://localhost:8000/api/data/'
#data = {
    #"ticker": "hello",
    #"x": "i'm from python",
    #"y": "this is working",
    #"owner": None
#}

url= "http://localhost:8000/api/scrape"

headers = {
    'content-type': 'application/json'
}

data = {
    'search': 'this is my data'
}

res = requests.post(url, data)

print(res.content)


