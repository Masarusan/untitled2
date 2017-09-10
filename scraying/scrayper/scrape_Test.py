# -*- coding: utf-8 -*-

from scrape_01 import Scrape


if __name__ == "__main__":
    sc = Scrape(url='http://xxeronetxx.info/img/20170906/v1-074.html')
    sc.scrape()
    # for a in sc.get_list():
    #     print(a)
    for a in sc.get_list_img():
        print("test:", a)