
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import math
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def create_quadratic(k, a, b):
	x_points = []
	y_points = []

	for x in range(-10, 11):
		x_points.append(x - a)
		y = k * (x ** 2) + b
		y_points.append(y)

	func_name = 'y = '
	if k != 1:
		func_name = func_name + str(k) + ' * '
	if a > 0:
		func_name = func_name + '(x - ' + str(a) + ')^2'
	elif a < 0:
		func_name = func_name + '(x + ' + str(a * -1) + ')^2'
	else:
		func_name = func_name + 'x^2'

	if b > 0:
		func_name = func_name +  ' + ' + str(b)
	elif b < 0:
		func_name = func_name + ' - ' + str(b * -1)

	plt.gcf().canvas.set_window_title(func_name)

	thismanager = plt.get_current_fig_manager()
	thismanager.window.wm_iconbitmap("docs/favicon.ico")

	plt.grid(color='k', linestyle='-', linewidth=0.5)

	plt.arrow(0, -1000, 0, 2000, fc='k', ec='k')
	plt.arrow(-1000, 0, 2000, 0, fc='k', ec='k')

	plt.plot(x_points, y_points, 'r')

	plt.title(func_name)
	plt.axis('equal')

	plt.show()

