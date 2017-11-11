answer = ["イギリス", "イギリス", "スペイン", "ドイツ", "フランス",
          "イギリス", "フランス", "フランス", "イギリス", "フランス", "フランス", "イギリス",
          "フランス", "フランス", "スペイン", "イタリア","イタリア", "スペイン", "イタリア",
          "スペイン", "イタリア", "イタリア", "スペイン", "イタリア", "イタリア", "イギリス",
          "スペイン", "ドイツ", "フランス", "フランス", "イタリア", "イタリア", "スペイン",
          "スペイン", "イタリア", "イタリア", "ドイツ","イタリア", "イタリア", "イタリア"]

#空の辞書を用意

results = {}

#辞書resultsに国と得票数を格納する
for country in answer:
    if country in results:
        results[country] +=1
    else:
        results[country]=1
#結果をソートして表示する

for country in sorted(results.items(),key = lambda  c:c[1],
                      reverse=True):
    print("{}:{}".format(country[0],country[1]))