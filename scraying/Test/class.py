# -*- coding: utf-8 -*-
class Rect:
    #インスタンスが作成された直後に呼び出される特殊なメソッドを定義する
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #面積を計算するメソッドを定義する
    def area(self):
        return self.width * self.height

r = Rect(100, 200)
print(r.width, r.height, r.area())

#Rectを継承したSquareクラスを定義する


class Square(Rect):
    def __init__(self, width):
        super.__init__(width, width)# 親クラスを呼び出し
if __name__ == "__main__":
   app = Square
   app2 = Rect