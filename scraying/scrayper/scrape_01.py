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
from datetime import datetime
import cchardet
from Csv_checker import Csv_Checker

class Scrape:
    #初期化
    def __init__(self, list=[[]], url=[''], soup='', response=""):
        self.__list = list
        self.__url = url
        self.__soup = soup
        self.__response = response
        self.__link = ""
        self.http_ok(self.__url)

    #httpの入力判定
    def http_ok(self, url):
        for urls in url:
            #p = re.compile('(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)')#http(s)正規表現
            root, ext = os.path.splitext(urls)
            if self.get_httppattern().match(urls):#http(s)の場合実行
                print('HTTP_PATTERN_OK')
                print('URL:{0}'.format(urls))#urlsから取得
                time.sleep(1)
                self.scrape(urls)
            elif ext in ".html":#ファイルの場合そのまま読み取る
                print("ローカルディレクトリからファイルを取得")
                try:
                    #self.file_open(self.get_url())
                    self.directory_htmlfile(urls)
                    #raise FileNotFoundError('TestError')
                except FileNotFoundError as a:
                    print("ファイルが見つかりませんでした")
                    print("FileNotFound:{0}".format(a))
                    #raise
            elif ext in ".csv":#Csvファイル読み取り
                print("CSV_file")
                csv_file = Csv_Checker(urls)
                #csv_file.csv_dict(urls)

            else:
                print('Error')
                sys.exit()

    # スクレイピングメソッド
    def scrape(self, url):
        #http = session.get(self.get_url(), timeout=1)
        MAX_RETRIES = 3
        retries = 0
        std = ''
        while True:
            try:
                s = requests.Session()
                header = {'User-Agent' : 'Plactice_Browser/0.01'}
                self.set_response(s.get(url, timeout=8, allow_redirects=False, stream=True, headers=header))
                ccencode = cchardet.detect(self.get_response().content)["encoding"]#エンコード判定
                self.__response.encoding = ccencode
                if self.get_response().status_code != requests.codes.ok:
                    sys.stdout.write('Error:')
                    sys.stdout.write('Status_Code:{0}'.format(self.get_response().status_code))
                    return False
                else:
                    print('Success!')
                    print('HTTP_STATUS_CODE:{0}'.format(self.get_response().status_code))
                    print('Encoding:{0}'.format(self.get_response().encoding))
                    print('Accesetime:{0}'.format(self.get_response().elapsed.total_seconds()))
                    self.set_soup(BeautifulSoup(self.get_response().content, 'html.parser'))
                    print('BS4_Original_encoding:{0}'.format(self.get_soup().original_encoding))
                    #self.__list = [[p] for p in self.get_soup().find_all(['img', 'src'])]
                    jpeg = re.compile(".jpg")
                    jpg = ".jpg"
                    #self.__list = [p for p in self.get_soup().find_all(['img', 'src'], string=True) if jpeg.match(str(p))]
                    #return True
                    #for p in self.get_soup().find_all('img', src = re.compile(".jpg")):
                        #self.set_link(p["src"])
                        #print(self.get_link())
                    self.csv_get(self.get_soup())

                    return


            except requests.exceptions.RequestException as ex:
                #ネットワークレベルのエラー
                print('Exception occured:{0}'.format(ex))
            retries+=1
            if retries >= MAX_RETRIES:
                raise Exception('Too many retries.')#リトライ回数の上限を超えた時例外発生

            wait = 2**(retries-1)
            std += '.'
            #sys.stdout.write('\rReConeccting %d seconds%s' % (wait,std))
            #print("\rReConnectiong {0}seconds{1}".format(wait, std),end='')
            #print()
            sys.stdout.flush()
            time.sleep(wait)#ウェイト

    #パース保持、自動整形してsoupに格納
    #ファイルを展開
    def directory_htmlfile(self, content):
        with open(content, 'rb')as f:
            parser = BeautifulSoup(f, 'html.parser')
            print(parser)
            return parser

    #使わない
    @staticmethod
    def encode_decision(self, soup):
        detector = UniversalDetector()
        for line in soup:
            detector.feed(line)
            if detector.done:
                break

            detector.close()
            print(detector.result)
            print(detector.result['encoding'], end='')
        return


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
        #p = re.compile('(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)')
        now = datetime.today()
        file_time = now.strftime("%Y-%m-%d %H:%M/")  # 保存日付
        filename = "image/"
        path = filename + file_time
        os.mkdir(path)
        files = glob.glob(filename + '/*')  # ディレクトリ
        #self.file_check()
        os.chdir(path)
        for links in self.get_soup().find_all('img', src = re.compile(".jpg")):
            self.set_link(links['src'])
            print(self.get_link())
            if self.get_httppattern().match(self.get_link()):
                with open(os.path.basename(self.get_link()), "wb")as f:
                    self.set_response(requests.get(self.get_link()).content)
                    linkUrl = "http:" + self.get_link()
                    self.set_link(linkUrl)
                    f.write(self.get_response())
                    time.sleep(2)
            else:
                pass

        return print("Finished")
    # ファイルをオープン

    def file_open(self, open_files):
        with open(open_files, "r", encoding="utf-8")as f:
            for i, line in enumerate(f):
                print("{:4d}:{}".format(i + 1, line.strip("\n")))

    #ディレクトリ作成、日時指定
    def file_check(self):
        now = datetime.today()
        file_directory = now.strftime("image/%Y-%m-%d %H:%M/")#保存日付
        if not os.path.exists(file_directory):#ディレクトリ、ファイルが存在しない場合ディレクトリを作成
            try:
                os.mkdir(file_directory)
                os.chdir(file_directory)
                if not os.path.isfile(file_directory):
                    return file_directory
                    pass
            except FileExistsError as e:
                print(e.errno)
                print(e.filename)
                sys.exit(1)
        else:
            print("Not Directory")

    #e-Stat人口統計
    def csv_get(self, soup):
        tmp_csv =  self.get_url()[0].rstrip('List.do?bid=000001034991')
        tmp_csvfile = './Csvdl.do?sinfid=000012460662'.lstrip('./')
        tmp_csv +=tmp_csvfile
        print(tmp_csv)
        print(type(tmp_csv))
        for csv in soup.find_all('a'):
            csv_file = csv.get('href')
            print(csv)
        pass

    #httpパターン

    def get_httppattern(self):
        self.__httppattern = re.compile('(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)')
        return self.__httppattern

    #5chスレッド取得メソッド
    def get_5ch(self):
        self.__link = self.__soup.find_all('div', class_='message')
        for i in self.get_link():
            print(i)

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
    def set_list(self, list):
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