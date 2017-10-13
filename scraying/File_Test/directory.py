# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime
import time
from shutil import copyfileobj, copyfile
from io import StringIO

class Directory():
    def derectory(self, filename):
        now = datetime.today()
        directory_time = now.strftime("../scrayper/image/%Y-%m-%d %H:%M")
        if not os.path.exists(directory_time):
            try:
                os.mkdir(directory_time)
                os.chdir(directory_time)
                if not os.path.isfile(directory_time):
                    with open(filename + '.txt', 'w')as f:
                        f.write("{}: おはよう".format(directory_time))


            except FileExistsError as e:
                print(e.errno)
                print(e.filename)
                sys.exit(1)
        else:
            os.chdir(directory_time)
            with open(filename + '.txt', 'w')as file:
                file.write("{}: Hello!!".format(directory_time))


if __name__ == "__main__":
    did = Directory()
    did.derectory("Test")
    # path = "../scrayper/image/"
    # path_2 = ""
    # now = datetime.today()
    # str = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    # #str = now.strftime("%Y-%m-%d %H:%M")
    # str_date = now.strftime("%Y-%m-%d %H:%M")
    # print(str_date)
    # print(str)
    # test = ''
    # #data = time.ctime(str)
    # dic_1 = path + str_date
    # if not os.path.exists(dic_1):
    #     try:
    #         os.mkdir(dic_1)
    #         os.chdir(dic_1)
    #         if not os.path.isfile(dic_1):
    #             with open(str_date + '.txt', 'w') as f:
    #                 f.write("こんばんは")
    #     except FileExistsError as e:
    #         print(e.errno)
    #         print(e.filename)
    #         sys.exit(1)
    # else:
    #     print("Error")
    #     lang = StringIO("Hello")
    #     os.chdir(dic_1)
    #     with open(str_date + '.txt', "w")as f:
    #         copyfileobj(lang, f)



