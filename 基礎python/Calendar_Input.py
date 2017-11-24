from calendar import TextCalendar

#年を変数Yearに格納する
year = int(input("年を入力してください："))

#月を変数monthに格納する
month = int(input("月を入力してください："))

cal = TextCalendar(6)
#cal.prmonth(year,month)
cal_str = cal.formatmonth(year,month)
print(cal_str)