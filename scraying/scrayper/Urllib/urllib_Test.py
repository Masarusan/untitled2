# -*- coding: utf-8 -*-

from urllib.request import urlopen
import os


url = "http://xxeronetxx.info/img/20170915/m-c057b12aec7f397866ce7ffd4ad140d35c592eaa.jpg"

any_url_obj = urlopen(url)#カレントディレクトリにダウンロード
local = open(os.path.basename(url), 'wb')
local.write(any_url_obj.read())

any_url_obj.close()
local.close()

if __name__ == "__main__":
    pass