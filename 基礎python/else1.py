words = ["旅行","桜","テレビ","終了","岸辺","ラジオ"]

for word in words:
    if word == "終了":
        print("*ループを中断しました")
        break
    print(word)
else:
    print("*ループが完了しました")