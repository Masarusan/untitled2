import customer_m1

taro = customer_m1.Customer(101, "斎藤太郎", 180)

hanako = customer_m1.Customer(102, "山田花子", 160)

print("{} 標準体重:{:.2f}kg".format(taro.name,
      taro.std_weight()))
print("{} 標準体重:{:.2f}kg".format(hanako.name,
      hanako.std_weight()))