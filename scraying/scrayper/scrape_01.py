# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class scrape():

    #初期化
    def __init__(self):
        self.__list = list

    def scrape(self):
        url = requests.get('http://xxeronetxx.info/img/20170906/v1-074.html', timeout=2)
        print('HTTP_STATUS_CODE:{}'.format(url.status_code))
        print('Encoding:{}'.format(url.encoding))
        print('Accesetime:{}'.format(url.elapsed.total_seconds()))
        soup = BeautifulSoup(url.content, 'html.parser')
        i = 0
        self.list = []
        for a in soup.find_all(['img', 'src']):
            print(i, ':', a.get('src'), a.text)
            self.list = soup.find_all('src')
            #self.list = soup.find_all('src')
            i += 1
            #print(i)

    #リストに格納したデータの取り出し
    def pop(self):
        for a in self.list:
            print(a.get('src'))
    #リストのgetter
    def get_list(self):
        return self.__list
    #リストのsetter
    def set_list(self):
        self.__list = list

if __name__ == "__main__":
     sc =  scrape()
     sc.scrape()
     print('list:', sc.get_list())
     print("抽出：",sc.get_list())