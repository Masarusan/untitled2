# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg') # 描画 の バック エンド として デスク トップ 環境 が 不要 な Agg を 使う。
#  日本語 を 描画 できる よう フォント を 指定 する。 OS X と Ubuntu 用 に 2 種類 の フォント を 列挙 し て いる。
#  デフォルト では 英語 用 の フォント が 使わ れ、 日本語 が □（ いわゆる 豆腐） で 表示 さ れ て しまう。
matplotlib.rcParams['font.sans-serif'] = 'Hiragino Kaku Gothic Pro, MigMix 1P'

#plot() の 第 3 引数 に 系列 の スタイル を 表す 文字列 を 指定 できる。
#  'b' は 青色、' x' は バツ 印 の マーカー、'-' は マーカー を 実線 で 繋ぐ こと を 意味 する。 # キーワード 引数 label で 指定 し た 系列 の 名前 は、 凡例 で 使用 さ れる。
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'bx-', label ='1次関数')
# スタイル の' r' は 赤色、' o' は 丸 印 の マーカー、'--' は 点線 を 意味 する。
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro--', label ='2次関数')
plt.xlabel('Xの値') # xlabel() 関数 で X 軸 の ラベル を 指定 する。
plt.ylabel('Yの値') # ylabel() 関数 で Y 軸 の ラベル を 指定 する。
plt.title('matplotlibのサンプル') # title() 関数 で グラフ の タイトル を 指定 する。
plt.legend(loc ='best') # legend() 関数 で 凡例 を 表示 する。 loc =' best' は
#最適 な 位置 に 表示 する こと を 意味 する。
plt.xlim( 0, 6) # X 軸 の 範囲 を 0 ～ 6 と する。
#  ylim() 関数 で 同様 に Y 軸 の 範囲 を 指定 できる。
plt.savefig('advanced_graph.png', dpi = 300) # グラフ を 画像 ファイル に 保存 する。
plt.show()

