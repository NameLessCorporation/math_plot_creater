
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import math
import numpy as np
from ezprint import *
from tkinter import *
from threading import Thread
import matplotlib.pyplot as plt

# Standart: y=k(x-a)+b
# With module: y=k|(x-a)|+b, then
# 1)y=k(-x-a)+b
# 2)y=k(x-a)+b

x_points = []
y_points = []


def create_plot(k, a, b):
	plt.grid(color='k', linestyle='-', linewidth=0.5)
	# With module: y=k*|(x-a)|+b, then
	if a < 0 and b < 0:
		func_name = 'y=' + str(k) + '|x-' + str(-a) + '|' + '-' + str(-b)
	elif a > 0 and b > 0:
		func_name = 'y=' + str(k) + '|x+' + str(a) + '|' + '+' + str(b)
	elif a < 0 and b > 0:
		func_name = 'y=' + str(k) + '|x-' + str(-a) + '|' + '+' + str(b)
	elif a > 0 and b < 0:
		func_name = 'y=' + str(k) + '|x+' + str(a) + '|' + '-' + str(-b)



	plt.gcf().canvas.set_window_title(func_name)

	plt.arrow(0, -10000, 0, 20000, fc='k', ec='k')
	plt.arrow(-10000, 0, 20000, 0, fc='k', ec='k')

	plt.plot(x_points, y_points, 'r')

	thismanager = plt.get_current_fig_manager()
	thismanager.window.wm_iconbitmap("docs/favicon.ico")

	plt.title(func_name)

	plt.axis('equal')

	plt.show()


def create_linear_with_module(k, a, b, lang):
	global y_points
	global x_points

	for i in np.arange(-10.0, 10.0, 0.1):
		x_points.append(i)

	for i in x_points:
		y = k * math.fabs((i - a)) + b
		y_points.append(y)
	create_plot(k, a, b)