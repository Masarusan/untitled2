# -*- coding: utf-8 -*-

import os.path

def main():
    root, ext = os.path.splitext('http://www.example.com/foo/bat/test.txt')
    print(root)
    print(ext)
if __name__ == "__main__":
    main()