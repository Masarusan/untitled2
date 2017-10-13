# -*- coding: utf-8 -*-
import requests
import os
from scrape_01 import Scrape
import time
from bs4 import BeautifulSoup

class image_scrape():
        
    def image_download(self, link=[[]]):

        url = ['']
        for i in link:
            res = requests.get(i).content
            filename = "image/"
            with open(filename + os.path.basename(i), "wb")as f:
                print(filename + os.path.basename(i))
                f.write(res)
                time.sleep(1)

if __name__ == "__main__":
    #ig = image_scrape()
    #sc = Scrape(url =")
    sc = Scrape()
    #ig.image_download(sc.get_link())
    # for i in sc.get_link():
    #     print(i)
    #print(sc.get_link())
    #print(sc.list_url())
    print(sc.file_check('image'))