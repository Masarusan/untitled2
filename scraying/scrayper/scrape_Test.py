# -*- coding: utf-8 -*-

from scrape_01 import Scrape
import sys
import time


if __name__ == "__main__":
    #sc = Scrape(url="/Users/masaru/gihyo.jp/dp/index.html")
    #sc = Scrape(url='http://xxeronetxx.info/img/20170906/v1-074.html')
    #sc = Scrape(url='http://httpbin.org/status/503,200,403')
    #sc.scrape()
    #sc.list_img()
    #sc = Scrape(url='/Users/masaru/gihyo.jp/dp/index.html')
    #sc.file_open(url="")
    #sc.list_img(sc.file_open("/Users/masaru/gihyo.jp/dp/index.html"))
    #'http://xxeronetxx.info/'
    # retries = 3
    # retries+=1
    # wait = 0
    # wait = 2**(retries-1)
    # print(wait)

    # for a in range(5):
    #     sys.stdout.write('.')
    #     sys.stdout.flush()
    #     time.sleep(1)
    #print("Test"+ sc.get_link()[0])
    #sc.downloading()
    sc = Scrape(url="http://xxeronetxx.info/img/20170906/v1-074.html")
    #print(sc.download(type(sc.get_link())))
    print(type(sc.get_link()))
    type(sc.get_link())
    print(sc.get_list())
