year = int(input("年を入力してください"))
if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        print(str(year) + "年は閏年です")
else:
    print(str(year) + "年は閏年ではありません")