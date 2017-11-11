# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import time

def spinner_gen():
    while 1:
        yield '|'
        yield '/'
        yield '-'
        yield '\\'


if __name__ == '__main__':
    for spinner in spinner_gen():
        time.sleep(0.05)
        print(spinner + '\033[1D', end='', file=sys.stderr)