# -*- coding: utf-8 -*-

import re
import sys
from urllib.request import urlopen

f = urlopen("http://sample.scrayping-book.com/dp")
bytes_content = f.read() #bytes型のレスポンスボディを一旦変数に格納する

#charsetはHTMLの最初のほうにッカれていると期待できるので、
#レスポンスボディの先頭1024バイトくぉASCII文字列としてデコードする
#ASCI範囲外の文字はU+FFFD(REPLACEMENT CHARACTER)に置き換え、例外を発生させない

scannned_text = bytes_content[:1024].decode("ascii", errors="replace")
#デコードした文字列から正規表現でcharsetの値を抜き出す
match = re.search(r'charset=["\']?([\w-]+)' ,scannned_text)
if match:
    encoding = match.group(1)

else:
    encoding = "utf-8" #charsetが明示されていない場合はUTF-8とする

print("encoding:", encoding, file=sys.stderr)
#得られたエンコーディングを標準エラー出力する。
text = bytes_content.decode(encoding)
# 得られたエンコーディングで再度デコードする。
print(text)#レスポンスボディを標準出力する
if __name__ == "__main__":
    pass