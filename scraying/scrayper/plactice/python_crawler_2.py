# -*- coding: utf-8 -*-

import requests
import lxml.html

response = requests.get('https://gihyo.jp/dp')
root = lxml.html.fromstring(response.content)
root.make_links_absolute(response.url) #全てのリンクを絶対パスに変換する

#id='listBook'である要素の子孫のa要素のみを取得する。
for a in root.cssselect('#listBook a[itemprop="url"]'):
    url = a.get('href')
    print(url)

if __name__ == "__main__":
    pass