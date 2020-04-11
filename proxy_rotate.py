import json 
import os
import time
import urllib
import bs4 as bs
import random 
def proxy_rotate(url):
    def json_load():
        with open("proxydictlist.json") as f:
            print("json file exists")
            time.sleep(1)
            proxies_list = json.load(f)
            return proxies_list

    def json_create():
        with open("proxydictlist.json", "w") as f:
            json.dump([], f)
            time.sleep(1)
            return

    if os.path.exists("proxydictlist.json"):
        proxies_list = json_load()

    else:
        print("json file doesn't exist creating json file ...")
        json_create()
        proxies_list = json_load()

    if proxies_list: ## check if proxies_list is empty or not
        for i in range(0, len(proxies_list)):
            try:
                pick = random.choice(proxies_list)

                ## configuring urllib for use with proxies
                proxy_support = urllib.request.ProxyHandler(pick)
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)

                ## requests
                req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
                sauce = urllib.request.urlopen(req, timeout=5).read()
                soup = bs.BeautifulSoup(sauce, 'lxml')
                print(soup)
                return soup
            except:
                ## proxies that do not work are removed from the list
                print(f"{pick} did not work")
                proxies_list.remove(pick)
                print(f"{pick} removed")
                print(len(proxies_list))
                with open('proxydictlist.json', 'w') as f:
                    json.dump(proxies_list, f)

    else: ## if proxies_list is empty, we get our proxies without configuring urllib for using proxies
        req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        sauce = urllib.request.urlopen(req).read()
        soup=bs.BeautifulSoup(sauce, 'lxml')
        print(soup)
        return soup 