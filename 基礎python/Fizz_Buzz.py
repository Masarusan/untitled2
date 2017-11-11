num = int(input("年齢を入力してください："))
for i in range(num):
        if((num % 3 == 0) or (num % 5 ==0) and(num >= 100)):
            print("Fizz")
