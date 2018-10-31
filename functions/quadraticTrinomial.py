
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
import matplotlib.pyplot as plt

from math import *
from ezprint import *
from tkinter import *
from threading import Thread
from descriptionFunctions.DescQuadraticTrinomial import *

x_list = x_points = np.arange(-5.0, 5.0, 0.1)
start_frame = None
thirdFrame = None
x_null_0 = 0
x_null_1 = 0
x_null_2 = 0
y_list = []
xo = 0
yo = 0
D = 0


def create_qt(a, b, c, lang):
	global start_frame
	global x_list
	global y_list

	func_name = 'y = '
	if a != 1:
		func_name = func_name + str(a) + ' * x^2'
	else:
		func_name = func_name + 'x^2'

	if b == 1:
		func_name = func_name + ' + x'
	elif b == -1:
		func_name = func_name + ' - x'
	elif b < 0:
		func_name = func_name + ' - ' + str(-b) + ' * x'
	elif b > 0:
		func_name = func_name + ' + ' + str(b) + ' * x'
	else:
		pass

	if c > 0:
		func_name = func_name + ' + ' + str(c)
	elif c < 0:
		func_name = func_name + ' - ' + str(-c)
	else:
		pass

	p(func_name)
	
	for k in x_list:
		func = a * k**2 + b * k + c
		y_list.append(func)
	plt.plot(x_list, y_list, 'r')
	plt.arrow(0, -1000, 0, 2000)
	plt.arrow(-1000, 0, 2000, 0)

	plt.gcf().canvas.set_window_title(func_name)

	plt.grid(color='k', linestyle='-', linewidth=0.5)

	plt.axis('equal')
	try:
		f(a, b, c)
		start_frame = threading.Thread(target= lambda : main_frame(a, b, c, D, xo, yo, x_null_0, x_null_1, x_null_2, x_list, y_list, lang, func_name))
		start_frame.start()
	except:
		pass
		
	plt.show()
	
	return x_list, y_list


def f(a, b, c):
	# a * x**2 + b * x + c
	global x_null_1
	global x_null_2
	global y_list
	global xo
	global yo
	global D

	#search tops
	xo = -b / (2 * a)
	yo = -((b**2 - 4 * a * c) / 4 * a)
	#search Disc.
	D = b**2 - 4 * a * c
	if D > 0:
		#search null func.
		x_null_1 = (-b + sqrt(D)) / (2 * a)
		x_null_2 = (-b - sqrt(D)) / (2 * a)
	elif D == 0:
		x_null_0 = -b / (2 * a)
	elif D < 0:
		pass