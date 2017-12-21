# -*- coding: utf-8 -*-
#!/usr/bin/python3
import sys
from concurrent.futures import ThreadPoolExecutor
from scrape_01 import Scrape
import feedparser
import threading


class multi_Test(Scrape):
    def __init__(self, url):
        self.__urls = url
        super().__init__(url=self.__urls)
        # executer =ThreadPoolExecutor(max_workers=3)
        # futures = ['']
        # for it in self.__urls:
        #     future = executer.submit(super().__init__(url=it), it)
        #     futures.append(future)
        #     for future in futures:
        #         print(future.result())
        #super().__init__(url=self.__urls)
    def main(self):
        #スクレイピングする対象
        #d = feedparser.parse('http://b.hatena.ne,jp/hotentry.rss')
        #urls = [entry.link for entry in d.entries]内包式
        #最大3スレッドで並行処理するためにEcecutorオブジェクトを生成
        executer = ThreadPoolExecutor(max_workers=3)
        #Futureオブジェクトを格納しておくためのリスト。
        '''futres = []
            for url in urls:
            関数の実行をスケジューリングし、Futureオブジェクトを得る
            submit()の第2引数移行はfetch_and_scraper()関数の引数として渡される
            futre = executer.submit(fetch_and_scrape, url)
            futures.append(future)
            for future in futures:
            Futreオブジェクトから結果(関数の戻り値を取得して表示する。)
            print(futre.result())
        '''
        #executer.submit()


if __name__ == "__main__":
    mlt = multi_Test(url=[''])
    for n in range(len(mlt.get_url())):
        p = threading.Thread(target=mlt.__init__(url=['']),
                             args=('I`m function %s %n'))
        print(p)
        p.start()