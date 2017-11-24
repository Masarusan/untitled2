# -*- coding: utf-8 -*-

import logging
import logging.config

class test_log():
    def log_log(self):
        logging.config.fileConfig("log/logging.conf")
        logging.error("test")

if __name__ == '__main__':
    ts = test_log()
    ts.log_log()
