from datetime import date


class Customer:
    bmi = 22

    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height

    def std_weight(self):
        return Customer.bmi*(self.height/100)**2
#メソッド定義


def show_info(self):
        print("{}:{}".format(self.number, self.name))

#メソッドを追加
Customer.show_info = show_info

#インスタンスを生成
taro = Customer(101, "斎藤太郎" ,180)
#追加したshow_info()メソッドを実行
taro.show_info()