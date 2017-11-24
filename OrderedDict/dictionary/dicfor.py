# -*- coding: utf-8 -*-


class Dic2:
    def __init__(self):
        self.main()

    def main(self):
        print("キーのループ")
        dic = {'key1': 110, 'key2': 270, 'key3': 350}
        for key in dic:
            print("{}".format(key)) # key1〜key3が出力される
            print("{}".format(dic[key])) # それぞれのkeyに対応する値が出力される

    def test(self):
        print("値のループ")
        dic = {'key1': 110, 'key2': 270, 'key3': 350}
        for value in dic.values():
            print("{}".format(value))  # 値が出力される

    @staticmethod
    def key_loop(self):
        print("キーと値のループ")
        dic = {'key1': 110, 'key2': 270, 'key3': 350}
        for key, value in dic.items(): #キーと値を両方ループ
            print("{} : {}".format(key, value))  # keyと値が出力される

    @staticmethod
    def loop_index():
        print("ループインデックスを取得する")
        dic = {'key1': 110, 'key2': 270, 'key3': 350}

        for i, value in enumerate(dic):
            print("{} : {}".format(i, value))  # ループインデックスと値が出力

        for i, (key, value) in enumerate(dic.items()):
            print("{} : {} : value : {}".format(i, key, value))  # ループインデックスとkeyと値が出力


if __name__ == "__main__":
    app = Dic2()
    Dic2.loop_index()
    pass;