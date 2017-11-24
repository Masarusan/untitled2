def test1(num):
    #関数の内部で引数を変更
    print("num:{}".format(id(num)))
    num += 10
    print("num:{}".format(id(num)))
n = 3#ｎの値が反映されていない
test1(n)
print(n)