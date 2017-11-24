import os
from os import path
#絶対パスファイル・ディレクトリを表示
print("絶対パス" + __file__)
#相対パス
print("相対パス：" + path.dirname(__file__))

#現在のファイルパスだけを表示　　実行中のスクリプトディレクトリ
print("実行中ディレクトリ：" + os.path.basename(__file__))

#ファイル拡張子なし
print(u"ディレクトリ拡張子なし：" + path.splitext(__file__)[0])
#ファイル名拡張子なし
print("拡張子なし:" + path.splitext(path.basename(__file__))[0])

print(__name__)