# -*- coding: utf-8 -*-
#スクレイピングimg & src
import requests
from bs4 import BeautifulSoup
from chardet.universaldetector import UniversalDetector
import re
import sys
import time
import os.path
import glob
from datetime import date
from datetime import datetime
from filecmp import cmp


class Scrape:
    #初期化
    def __init__(self, list=[[]], url='', soup='', response=""):
        self.__list = list
        self.__url = url
        self.__soup = soup
        self.__response = response
        self.__link = ""
        self.http_ok(self.__url)


    #httpの入力判定
    def http_ok(self, url):
        #url = self.get_url()
        p = re.compile('(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)')#http正規表現
        root, ext = os.path.splitext(url)
        if p.match(url):#httpの場合実行
            print('HTTP_PATTERN_OK')
            print('URL:{}'.format(self.get_url()))
            return self.scrape(url)
        elif ext == ".html":
            print("ローカルディレクトリからファイルを取得")
            try:
                self.file_open(self.get_url())
                #raise FileNotFoundError('TestError')
            except FileNotFoundError as a:
                print("ファイルが見つかりませんでした")
                print("FileNotFound:{0}".format(a))
                #raise
        elif ext == ".csv":
            pass

        else:
            print('Error')
            sys.exit()

    # スクレイピングメソッド
    def scrape(self, url):
        #http = session.get(self.get_url(), timeout=1)
        max_retries = 3
        retries = 0
        std = ''
        while True:
            try:
                s = requests.Session()
                self.set_response(s.get(url, timeout=5, allow_redirects=False, stream=True))
                if self.get_response().status_code != requests.codes.ok:
                    sys.stdout.write('Error:')
                    sys.stdout.write('Status_Code:{}'.format(self.get_response().status_code))
                else:
                    print('Success!')
                    print('HTTP_STATUS_CODE:{}'.format(self.get_response().status_code))
                    print('Encoding:{}'.format(self.get_response().encoding))
                    print('Accesetime:{}'.format(self.get_response().elapsed.total_seconds()))
                    self.set_soup(BeautifulSoup(self.get_response().content, 'html.parser'))
                    print('BS4_Original_encoding:{}'.format(self.get_soup().original_encoding))
                    #self.__list = [[p] for p in self.get_soup().find_all(['img', 'src'])]

                    return self.list_url()


            except requests.exceptions.RequestException as ex:
                #ネットワークレベルのエラー
                print('Exception occured:{0}'.format(ex))
            retries+=1
            if retries >= max_retries:
                raise Exception('Too many retries.')#リトライ回数の上限を超えた時例外発生

            wait = 2**(retries-1)
            std += '.'
            sys.stdout.write('\rReConeccting %d seconds%s' % (wait,std))
            sys.stdout.flush()
            time.sleep(wait)#ウェイト

    @staticmethod
    def encode_decision(self, soup):
        detector = UniversalDetector()
        for line in soup:
            detector.feed(line)
            if detector.done:
                break

            detector.close()
            print(detector.result)
        return

    #ファイルをオープン
    def file_open(self, open_files):
        with open(open_files, "r", encoding="utf-8")as f:
            for i, line in enumerate(f):
                print("{:4d}:{}".format(i + 1, line.strip("\n")))

    #画像ファイル名を決定
    def save_filename(self):
        pass

    #画像をファイルに保存
    def save_image(self, image, filename):
        with open(filename, 'wb')as f:
            f.write(image.encode('utf-8'))

    #urlアクセスのみを取得する
    def scrape_img(self):
        pass

    #画像リンクを取得
    def get_link(self):
        return self.__link

    #取得した画像リンクを格納
    def set_link(self, link):
        self.__link = link
    #Testうまくいった____画像ダウンロード＿＿＿＿

    def list_url(self):
        p = re.compile('(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)')
        now = datetime.today()
        str = now.strftime("%Y-%m-%d %H:%M/")  # 保存日付
        filename = "image/"
        path = filename + str
        os.mkdir(path)
        files = glob.glob(filename + '/*')  # ディレクトリ
        os.chdir(path)
        for links in self.get_soup().find_all('img'):
            self.set_link(links['src'])
            print(self.get_link())
            if p.match(self.get_link()):
                with open(os.path.basename(self.get_link()), "wb")as f:
                    self.set_response(requests.get(self.get_link()).content)
                    linkUrl = "http:" + self.get_link()
                    self.set_link(linkUrl)
                    f.write(self.get_response())
                    time.sleep(2)
            else:
                pass

            return print("Finished")
    #ディレクトリ作成、日時指定
    def file_check(self, filename):
        if not os.path.exists(filename):
            try:
                os.mkdir(filename)
                os.chdir(filename)
                if not os.path.isfile(filename):
                    return True
            except FileExistsError as e:
                print(e.errno)
                print(e.filename)
                sys.exit(1)
        else:
            print("Error")


    def get_filer(self):
        return self.__filer

    def set_filer(self, filer):
        self.__filer = filer
    #get_response
    def get_response(self):
        return self.__response
    #set_response
    def set_response(self, response):
        self.__response = response


    #後々List型にしよう
    #URL保持
    def get_url(self):
        return self.__url

    #URL保持
    def set_url(self, url):
        self.__url = url

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

    #file
    def get_file(self):
        return self.__file

    #file
    def set_file(self, file):
        self.__file = file

    def get_linkurl(self):
        return self.__linkurl

    def set_linkurl(self, linkurl):
        self.__linkurl = linkurl