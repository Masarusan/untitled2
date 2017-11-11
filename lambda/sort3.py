names = names = ["田中 一 郎-1979", "山田 花子-2000", "井上 太郎-1964",
                 "藤本 和 雄-1988", "大津 徹-1959","後藤 信-1980"]
def get_year(str):
    year = str[-4:]
    return int(year)
names.sort(key = get_year)
print(names)
