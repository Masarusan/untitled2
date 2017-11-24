address = ["東京都千代田区","千葉県船橋市","東京都杉並区","埼玉県"
                                       "大宮市",
           "東京都町田市","東京都西東京市","東京都大田区","神奈川県横浜市"]
#startwith()指定した文字列から始まる引数を指定した文字列かどうか調べる
tokyo = [town[3:] for town in address if town.startswith("東京都")]
print(tokyo)