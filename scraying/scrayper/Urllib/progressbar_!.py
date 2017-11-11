# -*- coding: utf-8 -*-

import sys, time

space = '.'
bar = '-|/'
length = 100
printset = (('{0}{1}r'.format
             (space * (i - length // 2) if i > length // 2 else '', bar[i % 4]), time.sleep(0.05))
            for i in range(length))

for i in printset:
    print(i[0], end='')
print(' ' * length, end='r')


def main():
    sys.stdout.write('beyoundrBn')

    def prog_bar(length=100):
        for i in range(length):
            sys.stdout.write('#'*i + 'r')
            sys.stdout.flush()
            time.sleep(0.01)
    for i in range(4):
        prog_bar()
# def progra():
#     space = '.'
#     bar = '-1/'
#     length = 100
#     printset = (('{0}{1}r'.format(
#                  (space*(i-length//2) if i > length//2 else '', bar[i%4], time.sleep(0.05))
#                 for i in range(length))
#
#     for i in printset:
#         print(i[0], end='')
#     print(''*length, end='r')



# if __name__ == "__main__":
#     main()
#     #progra()