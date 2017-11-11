# -*- coding: utf-8 -*-

import sys, time

space = '.'
bar = '-|/'
length = 100
printset = (('{0}{1}r'.format
             (space*(i - length // 2) if i > length // 2 else '', bar[i % 4]), time.sleep(0.05))
            for i in range(length))

for i in printset:
    print(i[0], end='')
print(' '*length, end='r')