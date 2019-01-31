
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import math
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt
from descriptionFunctions.DescCubic import *


def create_cubic(k, a, b, lang):
	x_points = []
	y_points = []
	print(a)

	x_points = np.arange(-1.5, 1.5, 0.1)
	new_x  = []
	for i in range(len(x_points)):
		# print(x_points[i] - a)
		new_x.append(x_points[i] + a)
		y = k * ((x_points[i]) ** 3) + b
		y_points.append(y)
	x_points = new_x

	func_name = 'y = '
	if k != 1:
		func_name = func_name + str(k) + ' * '
	if a > 0:
		func_name = func_name + '(x - ' + str(a) + ')^3'
	elif a < 0:
		func_name = func_name + '(x + ' + str(a * -1) + ')^3'
	else:
		func_name = func_name + 'x^3'

	if b > 0:
		func_name = func_name +  ' + ' + str(b)
	elif b < 0:
		func_name = func_name + ' - ' + str(b * -1)

	plt.gcf().canvas.set_window_title(func_name)

	thismanager = plt.get_current_fig_manager()
	thismanager.window.wm_iconbitmap("docs/favicon.ico")

	plt.grid(color='k', linestyle='-', linewidth=0.5)

	plt.arrow(0, -1000000, 0, 2000000, fc='k', ec='k')
	plt.arrow(-1000000, 0, 2000000, 0, fc='k', ec='k')

	plt.plot(x_points, y_points, 'r')

	plt.title(func_name)
	
	plt.axis('equal')

	try:
		start_frame = threading.Thread(target= lambda : main_frame(k, a, b, x_points, y_points, lang, func_name))
		start_frame.start()
	except:
		pass

	plt.show()