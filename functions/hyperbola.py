#!/usr/bin/python
# -*- coding: utf-8 -*-

# <--Import lib

import math
import decimal
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def creat_hyperbola(k, a, b):
    x_points = []
    y_points = []

    x_points = np.around(np.arange(-10, 10, 0.1), decimals=4)
    y_points = k / x_points - a + b

    func_name = 'y = '

    if a > 0:
        func_name = func_name + str(k) + '/(x - ' + str(a) + ')'
    elif a < 0:
        func_name = func_name + str(k) + '/(x + ' + str(a * -1) + ')'
    else:
        func_name = func_name + str(k) + '/x'

    if b > 0:
        func_name = func_name + ' + ' + str(b)
    elif b < 0:
        func_name = func_name + ' - ' + str(b * -1)

    os_x = [min(x_points) - 5, max(x_points) + 5]
    os_y = [np.amin(y_points) - 5, np.amax(y_points) + 5]

    plt.plot(os_x, [0, 0], '-b', markersize=30)
    plt.plot([0, 0], os_y, '-b', markersize=30)

    plt.plot(x_points, y_points, 'r')

    plt.gca().legend(('x', 'y', 'f(x)'))
    plt.title(func_name)
    plt.axis('equal')
    plt.show()
