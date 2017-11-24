weekdays = ["月曜日\n","火曜日\n","水曜日\n","木曜日\n",
           "金曜日\n","土曜日\n","日曜日\n"]

with open("day.txt","w",encoding="utf_8") as f:
    f.writelines(weekdays)