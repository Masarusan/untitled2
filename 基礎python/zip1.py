weekday1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
weekday2 = ["日", "月", "火", "水", "木", "金", "土"]

for (eng,jap) in zip(weekday1,weekday2):
    print(eng + ":" + jap)