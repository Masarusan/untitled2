# -*- coding: utf-8 -*-

import csv
#引数にencoding='utf-8-sig'でエンコーディングを設定
#utf-8,utf-8-sig,utf-16,Shift_JIS(CP932) cp932
with open('top_cities.csv', 'w', newline="", encoding='utf-8-sig') as f:
    #第1引数にファイルオブジェクトを、第2引数にフィールド名のリストを指定する。
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader()#1行目のヘッダーを出力する。
    #writerows()で複数行を一度に出力する。引数は辞書のリスト
    writer.writerows([
        {'rank':1,'city':'上海','population':24150000},
        {'rank':2,'city':'カラチ','population':23500000},
        {'rank':3,'city':'北京','population':21516000},
        {'rank':4,'city':'天津','population':14722100},
        {'rank':5,'city':'イスタンブル','population':14160467},
    ])
if __name__ == "__main__":
    pass