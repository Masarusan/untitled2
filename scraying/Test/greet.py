# -*- coding: utf-8 -*-

import sys

def greet(name):
    print("Hello, {0}".format(name))

if len(sys.argv) > 1:
    name = sys.argv[1]
    greet(name)
else:
    greet("World")

if __name__ == "__main__":
    pass