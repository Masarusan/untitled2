#空の辞書を用意
results = {}

with open("answer.txt","r",encoding="utf_8") as f:
    for line in f:
        country = line.rstrip("\n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1

#結果をソートして表示する
for country in sorted(results.items(),key = lambda  c:c[1],
                      reverse=True):
    print("{}:{}".format(country[0],country[1]))
