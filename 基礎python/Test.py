from calendar import TextCalendar
print("おはよう",end="")
print("1:")
cal = TextCalendar(6)
cal.prmonth(2016,1)

height = float(input("身長(cm)を入力してください: "))
bmi = 22
std_weight = bmi * (height / 100) ** 2
print(" 身長: " + str(height) + "cm → ", end ="")
print(" 標準体重: " + str(std_weight) + "kg")
