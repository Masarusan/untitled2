class Customer:
    bmi = 22

    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height

#標準体重を戻す
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
#インスタンスを生成
taro = Customer(101, "斎藤太郎", 180)
hanako = Customer(102, "山田花子", 160)
#標準体重を表示
print("{}標準体重:{:.2f}kg".format(taro.name,
      taro.std_weight()))
print("{}標準体重:{:.2f}kg".format(hanako.name,
      hanako.std_weight()))