from datetime import date
class Customer:
    bmi = 22

    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height

    def std_weight(self):
        return Customer.bmi*(self.height/100)**2
#クラス変数を追加
Customer.LIMIT = 50
#インスタンスを生成
taro = Customer(101, "斎藤太郎" ,180)
hanako = Customer(102, "山田花子", 150)

#インスタンス変数を追加
print(taro.LIMIT)
print(hanako.LIMIT)
print(Customer.LIMIT)