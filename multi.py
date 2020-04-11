from multiprocessing import Pool, Process
from amazon_scrape import amazon_scrape
from ebay_scrape import ebay_scrape
import time 
if __name__ == '__main__':
    start_time = time.time()
    p1 = Process(target=amazon_scrape)
    p1.start()
    p2 = Process(target=ebay_scrape)
    p2.start()
    p3 = Process(target=amazon_scrape)
    p3.start()
    p4 = Process(target=ebay_scrape)
    p4.start()


    p1.join()
    p2.join()
    p3.join()
    p4.join()
    end_time = time.time() - start_time
    print(end_time)
    time.sleep(5)

    start_time = time.time()
    amazon_scrape()
    ebay_scrape() 
    amazon_scrape()
    ebay_scrape() 
    end_time = time.time() - start_time
    print(end_time)