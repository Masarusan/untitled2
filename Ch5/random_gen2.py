import  random
def random_gen(num):
    #生成済みの乱数を格納するリスト
    randoms = []

    while True:
        rand_num = random.randrange(num)
        #乱数に重複がない場合
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield  rand_num
            #全ての乱数を生成した
        elif len(randoms) == num:
            break
rand = random_gen(100)
for r in rand:
    print(r)