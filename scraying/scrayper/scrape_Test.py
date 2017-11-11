# -*- coding: utf-8 -*-

from scrape_01 import Scrape
import sys
import time

#CommandLine
def main():
    argc = sys.argv
    argv = len(argc)
    if (argc != 1):
        # 引数がちゃんとあるかチェック
        # 正しくなければメッセージを出力して終了
        sc = Scrape(url=[argc[1]])
        print('\nUsage: python{}arg1 arg2'.format(argv))
        quit()

if __name__ == "__main__":
    #sc = Scrape(url='http://httpbin.org/status/503,200,403')
    #sc = Scrape(url=["https://egg.5ch.net/test/read.cgi/game/1505885726/l50","http://matsuri.5ch.net/test/read.cgi/lic/1508063421/"])
    #print(sc.get_link())
    #sc = Scrape(url=["http://eropasture.com/archives/57223406.html"])
    #print(sc.file_check())
    #print(sc.get_list())
    main()