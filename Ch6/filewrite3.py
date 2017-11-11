import os,sys,random

#引数が一つであることを確認
if len(sys.argv) != 2:
    print("ファイル名を一つに指定してください")
    sys.exit()

#パスが存在するかを確認
path = sys.argv[1]
if os.path.exists(path):
    if input("上書きしますか？(y/n):") != "y":
        sys.exit()

kujis = ["大吉","中吉","凶"]
with open(path ,"w",encoding="utf_8") as f:
    f.write(kujis[random.randrange(len(kujis))] + "\n")

