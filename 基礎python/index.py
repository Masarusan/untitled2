words = ["空","秘密","電柱","開けゴマ","海","ギター"]
str1 = input("文字列を入力してください：")

try:
    index=words.index(str1)
    print('"{}のインデックスは{}です'.format(str1, index))
except ValueError:
    print('"{}は見つかりませんでした'.format(str1))
