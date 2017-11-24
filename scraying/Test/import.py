# -*- coding: utf-8 -*-
import sys #sysモジュールを現在の名前空間にインポート
from datetime import date
#datetimeモジュールから、dateクラスだけを現在の名前空間にインポート
print(sys.argv) #sysモジュールのargvという変数で、コマンドライン引数のリストを取得して表示する

print("{}".format(date.today()))

if __name__ == "__main__":
    pass