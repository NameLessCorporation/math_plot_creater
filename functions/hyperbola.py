
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import math
import decimal
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def create_hyperbola(k, a, b):
	x_points = []
	y_points = []

	x_points = np.around(np.arange(-10, 10, 0.1), decimals=4)
	y_points = (k / x_points - a) + b

	func_name = 'y = '

	if a > 0:
		func_name = func_name + str(k) + '/(x - ' + str(a) + ')'
	elif a < 0:
		func_name = func_name + str(k) + '/(x + ' + str(a * - 1) + ')'
	else:
		func_name = func_name + str(k) + '/x'


	if b > 0:
		func_name = func_name +  ' + ' + str(b)
	elif b < 0:
		func_name = func_name + ' - ' + str(b * -1)

	plt.gcf().canvas.set_window_title(func_name)

	plt.grid(color='k', linestyle='-', linewidth=0.5)

	plt.arrow(0, -10000, 0, 20000, fc='k', ec='k')
	plt.arrow(-10000, 0, 20000, 0, fc='k', ec='k')
	
	plt.plot(x_points, y_points, 'r')

	plt.title(func_name)
	plt.axis('equal')
	plt.show()