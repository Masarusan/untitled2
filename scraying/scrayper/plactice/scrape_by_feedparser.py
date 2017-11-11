# -*- coding: utf-8 -*-


import feedparser

#はてなブックマークの人気エントリー(「テクノロジー」カテゴリー)のRSSを読み込む。
d = feedparser.parse('http://b.hatena.ne.jp/hotentry/it.rss')

#全ての要素について処理をくり消す。
for entry in d.entries:
    print(entry.link, entry.title)

if __name__ == "__main__":
    pass