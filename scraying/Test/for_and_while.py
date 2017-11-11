# -*- coding: utf-8 -*-

for x in [1,2,3]:
    print(x)

for i in range(10):#組み込み関数range()
    print(i)

d = {"a":1,"b":2}
for key in  d:
    value = d[key]
    print("{}:{}".format(key, value))
#dictのitems()メソッドで、dictのキーと値に対して繰り返す
for key, value in d.items():
    print("dict : {}:{}".format(key, value))

#while文で式、真の間、繰り返し処理する
s = 1
while s < 1000:
    print(s)#2の倍数を表示
    s = s* 2

if __name__ == "__main__":
    pass