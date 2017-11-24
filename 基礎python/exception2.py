import sys

try:
    score = int(input("点数を入力してください："))
except:
    print("数値を入力してください")
else:
    print("入力した点数：",score)

if score >= 80:
        print("合格です")
else:
        print("不合格です")