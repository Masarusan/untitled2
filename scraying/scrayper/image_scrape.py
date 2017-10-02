# -*- coding: utf-8 -*-
import requests
import os
from scrape_01 import Scrape
import time
from bs4 import BeautifulSoup

class image_scrape():
        
    def image_download(self, link=[[]]):

        url = ['http://xxeronetxx.info/img/20170906/v1-074.html']
        for i in link:
            res = requests.get(i).content
            filename = "image/"
            with open(filename + os.path.basename(i), "wb")as f:
                print(filename + os.path.basename(i))
                f.write(res)
                time.sleep(1)

if __name__ == "__main__":
    ig = image_scrape()
    sc = Scrape(url ="http://xxeronetxx.info/img/20170906/v1-074.html")
    #ig.image_download(sc.get_link())
    # for i in sc.get_link():
    #     print(i)
    #print(sc.get_link())
    #print(sc.list_url())