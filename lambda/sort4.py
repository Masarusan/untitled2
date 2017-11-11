names = ["田中 一 郎-1979", "山田 花子-2000", "井上 太郎-1964", "藤本 和 雄-1988", "大津 徹-1959", "後藤 信-1980"]

names.sort(key = lambda str:int(str[-4:]))
print(names)