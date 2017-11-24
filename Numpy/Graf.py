# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def main():
    z = -1
    i = 3
    x = np.linspace(0, 5, 5) # 0～3まで20刻みでxの値を生成
    y = 2*(x**2+1) +3           # 曲線の式(2次関数)
    plt.plot(x, y, "r-")      # 曲線を引く
    plt.show()              # グラフ表示


if __name__ == '__main__':
    main()