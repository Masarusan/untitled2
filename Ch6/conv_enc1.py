import os,sys

#引数が２つであることを確認する
if len(sys.argv)!= 3:
    print("使い方: conv_enc1.py file1 file2")
    sys.exit()

#変換元のファイルが存在することを確認する
in_file = sys.argv[1]
if not os.path.exists(in_file):
    print("ファイルが存在しません")
    sys.exit()

#変換先のファイルが存在していた場合に上書きするかを確認する
out_file = sys.argv[2]
if os.path.exists(out_file):
    if input("上書きしますか？(y/n):") != "y":
        sys.exit()

#文字エンコードを入力する
print("文字エンコードをしていしてください");
enc_num = input("1:ShiftJIS 2:EUC-JP 3:JIS :")
enc = ""
if enc_num =="1":
    enc = "shift_jis"
elif enc_num =="2":
    enc = "euc_jp"
elif enc_num == "3":
    enc = "iso2022_jp"
else:
    print("エンコーディングが正しくありません")
    sys.exit()

#文字エンコーディングを変換する
with open(in_file,"r",encoding="utf_8") as in_f:
    with open(out_file,"w",encoding=enc) as out_f:
        for str in in_f:
            out_f.write(str)