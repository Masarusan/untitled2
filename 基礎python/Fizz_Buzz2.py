num = int(input("Fizz&Buzz："))
for i in range(num):
        if((i % 3 == 0) or (i % 5 ==0)):#3と５の公倍数
                print("Fizz")
        else:
            print("Buzz")
