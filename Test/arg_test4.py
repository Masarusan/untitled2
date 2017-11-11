def test3(lst):
    print("lst:{}".format(id(lst)))
    lst = lst + [3,4]
    print("lst:{}".format(id(lst)))

l = [1,2,3]
test3(l)
print(l)