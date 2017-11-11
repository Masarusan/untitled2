# -*- coding: utf-8 -*-

import re
from html import unescape

#前節でダウンロードしたファイルを開き、中身を変数に格納する

with open('dp.html') as f:
    html = f.read()

#re.findall()を使って、書籍1冊に相当するHTMLを取得する。
#*?は*と同様だが、なるべく短い文字列にマッチする(non-greedy)であることを表すメタ文字

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>',
                               html, re.DOTALL):
    #書籍URLはitemprop="url"という属性を持つa要素のhref属性から取得する
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    url = 'http://sample.scrayping-book.com/dp ' + url #/で始まっているのでドメイン名などをつかする。

    #書籍のタイトルはitemprop="name"という属性を持つp要素から取得する。
    title = re.search(r'<p itemprop="name".*?</p>',
                      partial_html).group(0)
    title = title.replace('<br/>', '')
    #</br>タグをスペースに置き換えるstr.replace()は文字列を置換する。
    title = re.sub(r'<.*?>', '', title)#タグを取り除く
    title = unescape(title)#文字参照を元に戻す。

    print(url, title)


if __name__ == "__main__":
    pass