# -*- coding: utf-8 -*-


def main():
    data_dict = {'apple': 100, 'orange': 80, 'banana': 70}
    for key, val in data_dict.items():
        print(key, val) # 実行するたびに順序が変わる

if __name__ == "__main__":
    main()