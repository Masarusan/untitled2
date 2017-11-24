# -*- coding: utf-8 -*-

from scrape_01 import Scrape
import sys
import time
import argparse
END = 170

MAX_LEN = 30

#CommandLine(コマンドラインからの入力)
class commandLine:

    def main(self):
        #parser = argparse.ArgumentParser(description='Process some Strings.')
        #parser.add_argument()
        #args = parser.parse_args()
        argc = sys.argv
        argv = len(argc)
        if (argv != 1):
            # 引数がちゃんとあるかチェック
            # 正しくなければメッセージを出力して終了
            sc = Scrape(url=[argv[1]])
            #入力引数確認用
            #print('\nUsage: python{}arg1 arg2'.format(argv))
            quit()

    def get_progressbar_str(progress):
        BAR_LEN = int(MAX_LEN * progress)
        return ('[' + '=' * BAR_LEN +
                ('>' if BAR_LEN < MAX_LEN else '') +
                ' ' * (MAX_LEN - BAR_LEN) +
                '] %.1f%%' % (progress * 100.))




if __name__ == "__main__":
    #sc = Scrape(url='http://httpbin.org/status/503,200,403')
    #sc = Scrape(url=["https://egg.5ch.net/test/read.cgi/game/1505885726/l50","http://matsuri.5ch.net/test/read.cgi/lic/1508063421/"])
    #print(sc.get_link())
    #sc = Scrape(url=["http://eropasture.com/archives/57223406.html"])
    #print(sc.file_check())
    #print(sc.get_list())
    cmd = commandLine()
    for i in range(END + 1):
        time.sleep(0.01)
        progress = 1.0 * i /END
        cmd.main()
        sys.stderr.write('\r\033[K' + cmd.get_progressbar_str(progress))
        sys.stderr.flush()
    sys.stderr.write('\n')
    sys.stderr.flush()
