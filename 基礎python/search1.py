#検索される文字列

str1 = "水金地火木土"
#検索対象の文字列
str2 = input("検索文字列を入力してください：")

if str2 in str1:
    print("" + str2 + "が見つかりました")
else:
        print("" + str2 + "が見つかりませんでした")