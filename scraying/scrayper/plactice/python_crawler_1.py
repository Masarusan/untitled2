# -*- coding: utf-8 -*-

import requests
import lxml.html

response = requests.get('https://gihyo.jp/dp')
root = lxml.html.fromstring(response.content)
for a in root.cssselect('a[itemprop="url"]'):
    url = a.get('href')
    print(url)


if __name__ == "__main__":
    pass