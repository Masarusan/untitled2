from customer_m1 import Customer

taro = Customer(101, "斎藤太郎", 180)
hanako = Customer(102, "山田花子", 179)

print("{}標準体重:{:.2f}kg".format(taro.name,
      taro.std_weight()))
print("{}標準体重:{:.2f}kg".format(hanako.name,
      hanako.std_weight()))