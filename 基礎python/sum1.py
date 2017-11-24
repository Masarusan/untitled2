end = int(input("最後の数値を入力してください："))

sum = 0
for num in range(1,end+1):
    sum+=num

    print(str(end) + "までの総和：",sum)