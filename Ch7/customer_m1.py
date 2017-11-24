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

    #プロパティ
    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)

