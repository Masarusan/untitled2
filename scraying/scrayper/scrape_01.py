# -*- coding: utf-8 -*-
#スクレイピングimg & src
import requests
from bs4 import BeautifulSoup
import re
import os


class Scrape:
    #初期化
    def __init__(self, list=[[]], url='', soup='', list_img=[[]]):
        self.__list = list
        self.__url = url
        self.__soup = soup
        self.__list_img = list_img
    #スクレイピングメソッド

    def scrape(self):
        #self.set_url(url)
        http = requests.get(self.get_url(), timeout=1)
        if http.status_code != requests.codes.ok:
            print('Error')
            exit(1)
        print('HTTP_STATUS_CODE:{}'.format(http.status_code))
        print('Encoding:{}'.format(http.encoding))
        print('Accesetime:{}'.format(http.elapsed.total_seconds()))
        self.set_soup(BeautifulSoup(http.content, 'html.parser'))

        self.__list = [[a] for a in self.get_soup().find_all(['img','src'])]
            #print(i, ':', a.get('src'), a.text)

        for link in self.get_soup().find_all('img'):
            self.__list_img = [link.get('src')]
            print(self.__list_img)

        print(type(self.__list))
    #画像ダウンロード
    def downloading(self, url, timeout=10):
        response = requests.get(url, allow_redirects=False, timeout=timeout)
        if response.status_code != 200:
         e = Exception("HTTP status:" + response.status_code)
         raise e
        content_type = response.headers["content-type"]
        if 'image' not in content_type:
            e = Exception("Content-Type:" + content_type)
            raise e
        return response.content

    #画像ファイル名を決定
    def save_filename(self):
        pass

    #画像をファイルに保存
    def save_image(self):
        pass

    #urlアクセスのみを取得する
    def scrape_img(self):
        pass

    #タグ'src'を格納
    def get_list_img(self):
        return self.__list_img

    def set_list_img(self, list_img):
        self.__list_img = list_img

    def scrape_console(self, soup):
        pass

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    #リストに格納したデータの取り出し
    def pop(self):
                #リンクを取得
        for a in self.__list:
            print('{}'.format(a.get('src')))
        #print(a.get('src'))

    #リストのgetter
    def get_list(self):
        return self.__list
    #リストのsetter
    def set_list(self):
        self.__list = list

    #html content get
    def get_soup(self):
        return self.__soup
    #html content set

    def set_soup(self, soup):
        self.__soup = soup


