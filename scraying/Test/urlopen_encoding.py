# -*- coding: utf-8 -*-

import sys
import ssl
from  urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context


f = urlopen("http://sample.scraping-book.com/dp")

#ret = requests.get(f, verify=False)

#HTTPヘッダーからエンコーディングを取得する（明示されていない場合Utf-8とする）
encoding = f.info().get_content_charset(failobj="utf-8")
print("encoding:", encoding, file=sys.stderr)#エンコーディングを標準エラー出力に出力する

text = f.read().decode(encoding)#得られたエンコーディングを指定した
print(text)
#デコードしたレスポンスボディを標準出力に出力する

if __name__ == "__main__":
    pass