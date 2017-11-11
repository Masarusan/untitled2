def doll_to_yen(doll,rate):
    return doll*rate
#引数にリテラルを指定して喚びだす
yen  = doll_to_yen(doll =100,rate = 105)
print("為替レート:{}".format(105))
print("{}ドルは{}円".format(100,yen))

rate = 100
doll = 150
#引きsに変数をしてして呼び出す
yen = doll_to_yen(doll = doll,rate = rate)
print("為替レート:{}".format(rate))
print("{}ドルは{}円".format(doll,yen))