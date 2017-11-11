class Customer:
    bmi = 22
    def __init__(self,number,name,height= 0):
        self.number = number
        self.name = name
        self.height = height

#クラス変数の値を表示
print("bmi:{}".format(Customer.bmi))

#インスタンスを生成
taro = Customer(101,"斎藤太郎",180)
hanako = Customer(102,"山田花子",165)
#クラス変数の値を変更
Customer.bmi = 23
print("taro -> bmi:{}".format(taro.bmi))
print("hanakko -> bmi:{}".format(hanako.bmi))