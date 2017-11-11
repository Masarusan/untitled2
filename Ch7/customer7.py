from datetime import date


class Customer:
    bmi = 22

    def __init__(self, number, name, height=0):
        self._number = number
        self._name = name
        self._height = height

    def std_weight(self):
        return Customer.bmi*(self.height/100)**2

    #nameのゲッターメソッド
    def get_name(self):
        return self._name;

    #numberのゲッターメソッド
    def get_number(self):
        return self._number

    #numberのセッターメソッド
    def set_number(self, number):
        self._number = number

    #heightのゲッターメソッド
    def get_height(self):
        return self._height

#インスタンスを生成
taro = Customer(101, "斎藤太郎", 180)

#name = taro._name;
#number = taro._number

#インスタンス変数を追加
name = taro.get_name()
taro.set_number(99)
number = taro.get_number()
height = taro.get_height()
taro.birthdate = date(1989, 7, 3)
print("{}:{}{}cm".format(number, name,
      height))