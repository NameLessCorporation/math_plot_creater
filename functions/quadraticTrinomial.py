
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
from math import *
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt
from descriptionFunctions.DescQuadraticTrinomial import *

x_list = x_points = np.arange(-5.0, 5.0, 0.1)
thirdFrame = None
x_null_0 = 0
x_null_1 = 0
x_null_2 = 0
y_list = []
xo = 0
yo = 0
D = 0


def create_qt(a, b, c):
	global x_list
	global y_list

	for k in x_list:
		func = a * k**2 + b * k + c
		y_list.append(func)
	plt.plot(x_list, y_list)
	plt.arrow(0, -1000, 0, 2000)
	plt.arrow(-1000, 0, 2000, 0)
	plt.axis('equal')
	plt.show()
	f(a, b, c)
	main_frame(a, b, c, D, xo, yo, x_null_0, x_null_1, x_null_2, x_list, y_list)
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
		p('Discriminant < 0')