#集合の内包表記を使用する
lst = [100,200,100,200,300,400,90,100,50]

num = {num for num in lst if num > 100}
#100以上を抽出する
print(num)