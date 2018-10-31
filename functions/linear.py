
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
from ezprint import *
from tkinter import *
from threading import Thread
import matplotlib.pyplot as plt
from descriptionFunctions.DescLinear import *


def create_linear(k, a, b, lang):
	x_points = []
	y_points = []

	for x in range(-10, 11):
		x_points.append(x - a)
		y = k * x + b
		y_points.append(y)

	func_name = 'y = '
	if k != 1:
		func_name = func_name + str(k) + ' * '
	if a > 0:
		func_name = func_name + '(x - ' + str(a) + ')'
	elif a < 0:
		func_name = func_name + '(x + ' + str(a * -1) + ')'
	else:
		func_name = func_name + 'x'


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

	start_frame = threading.Thread(target= lambda : desc(k, a, b, lang, func_name))
	start_frame.start()

	plt.show()

