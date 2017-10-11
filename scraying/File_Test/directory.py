# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime
import time

if __name__ == "__main__":
    path = "../scrayper/image/"
    path_2 = "../scrayper/image/m-38e8702150edfc170f45fb1c8dd84765bdd57989.jpg"
    print(os.path.exists(path))
    print(os.path.isfile(path_2))
    print(os.path.isdir(path))
    print(datetime.today().month)
    print(datetime.today().date())
    now = datetime.today()
    str = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    #str = now.strftime("%Y-%m-%d %H:%M")
    str_date = now.strftime("%Y-%m-%d %H:%M")
    print(str_date)
    print(str)
    #data = time.ctime(str)
    dic_1 = path + str_date
    if not os.path.exists(dic_1):
        try:
            os.mkdir(dic_1)
            os.chdir(dic_1)
            if not os.path.isfile(dic_1):
                with open(str_date + '.txt', 'w') as f:
                    f.write("こんばんは")
        except FileExistsError as e:
            print(e.errno)
            print(e.filename)
            sys.exit(1)
    else:
        print("Error")


