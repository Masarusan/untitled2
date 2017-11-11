# -*- coding: utf-8 -*-


class Dic1:

    def __init__(self):
        self.dic = {"key1": 110, "key2": 270, "key3": 350}
        print(self.dic)

        def __init__(self):
            print("Test")

    def main(self):
        dic = {"key1": 110, "key2": 270, "key3": 350}
        print(dic)
        print(dic["key1"])
        #print(dic["hoge"])
        dic["key1"] = 200 #値を更新
        print(dic["key1"])
        print(len(dic)) #要素数
if __name__ == "__main__":
    app = Dic1()
    app.main()
