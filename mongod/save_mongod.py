# -*- coding: utf-8 -*-


import lxml.html
from pymongo import MongoClient

#HTMLファイルを読み込み、getroot()メソッドでHtmlElementオブジェクトを得る
tree = lxml.html.parse('/Users/masaru/gihyo.jp/dp/index.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)
db = client.scraping #scrapingデーターベースを取得する。
collection = db.links #linksコレクションを取得する。
#このスクリプトを何回実行しても同じ結果になるようにするために、コレクションのドキュメントをすべて削除する。
collection.delete_many({})

#cssselect()メソッドでa要素のリストを取得して、個々のa要素に対して処理を行う。
for a in html.cssselect('a'):
    #href属性とリンクのテキストを取得して保存する。
    collection.insert_one({
        'url':a.get('href'),
        'title':a.text,
})
#コレクションの全てのドキュメントを_idの順にソートしてしゅとくする。
for link in collection.find().sort('_id'):
    print(link['_id'],link['url'], link['title'])


if __name__ == "__main__":
    pass