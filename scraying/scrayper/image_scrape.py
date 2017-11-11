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
    sc = Scrape(url=["/Users/masaru/Downloads/Empyrion共有翻訳所Part2 - PDA翻訳作業用シート .csv"])