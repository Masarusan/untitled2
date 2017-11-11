class Customer:
    def __init__(self,number,name,height = 0):
        self.number = number
        self.name = name
        self.height = height

#インスタンスを生成
taro = Customer(1101,"斎藤太郎",180)
print("{}:{}{}cm".format(taro.number,taro.name,
                         taro.height))
taro.height = 175
print("{}:{}{}cm".format(taro.number,taro.name,
                         taro.height))