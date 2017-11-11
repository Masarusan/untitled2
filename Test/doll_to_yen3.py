def doll_to_yen(doll,rate=100):
    return doll*rate

#ふたつの引数を指定して喚びだす
doll1 = 100
yen = doll_to_yen(doll1,105)
print("為替レート:{}".format(105))
print("{}ドルは{}円".format(doll1,yen))

#引数rateを省略して喚びだす
doll2 = 50
yen = doll_to_yen(doll2)
print("為替レート:{}".format(100))
print("{}ドルは{}円".format(doll2,yen))