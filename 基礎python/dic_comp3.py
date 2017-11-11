#辞書のキーと値を入れ替える
seasons1 = {'Summer':'夏','Autumn':'秋','Winter':'冬',
    'Spring':'春'}

seasons2 = {j:e for(e,j) in seasons1.items()}
#items()で要素を取り出す.j:e e,jとで入れ替え作業
print(seasons2)