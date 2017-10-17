# -*- coding: utf-8 -*-

from scrape_01 import Scrape
import sys
import time


if __name__ == "__main__":
    #sc = Scrape(url='http://httpbin.org/status/503,200,403')
    sc = Scrape()
    sc.file_check("image/")



