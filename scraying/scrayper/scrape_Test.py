# -*- coding: utf-8 -*-

from scrape_01 import Scrape
import sys
import time


if __name__ == "__main__":
    #sc = Scrape(url="")
    #sc = Scrape(url='')
    #sc = Scrape(url='http://httpbin.org/status/503,200,403')
    #sc.scrape()
    #sc.list_img()
    #sc = Scrape(url='')
    #sc.file_open(url="")
    #sc.list_img(sc.file_open(""))
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
    #sc = Scrape(url="")
    #sc = Scrape(url="")
    #print(sc.download(type(sc.get_link())))
    #print(type(sc.get_link()))
    #type(sc.get_link())
    #print(sc.file_check('image'))
    #print(sc.get_link())
    #print(type(sc.get_link()))
    #print(sc.get_linkurl())
    #print(sc.get_link())
    sc = Scrape()
    sc.file_check("image/")



