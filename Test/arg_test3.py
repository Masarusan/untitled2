def test2(lst):
    print("lst:{}".format(id(lst)))
    lst[0] = 0#要素を変更する
    lst.append(100)#要素を追加する
    print("lst:{}".format(id(lst)))

l = [1,2,3]
test2(l)
print(l)