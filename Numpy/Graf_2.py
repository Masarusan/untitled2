# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def f(x):
    return x**2 + 2 * x + 1


def z(x):
    return 2*(x+1)**2+3


def draw_graph():
    plt.figure(figsize=(5, 5))
    xs = range(-100, 101)
    ys = map(z, xs)
    plt.plot(list(xs), list(ys))
    plt.axis(ymin=-2000)
    plt.title('y = x**2 + 2*x + 1')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('quadratic.png')
    plt.show()

if __name__ == '__main__':
    draw_graph()