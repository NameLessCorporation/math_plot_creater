
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import math
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def create_sin(k, a, b):
	x_points = []
	y_points = []

	x_points = np.arange(-10.0, 10.0, 0.1)
	new_x  = []
	for i in range(len(x_points)):
		new_x.append(x_points[i] - a)
		y = k * (math.sin(x_points[i])) + b
		y_points.append(y)
	x_points = new_x

	func_name = 'y = '
	if k != 1:
		func_name = func_name + str(k) + ' * '
	if a > 0:
		func_name = func_name + 'sin(x - ' + str(a) + ')'
	elif a < 0:
		func_name = func_name + 'sin(x + ' + str(a * -1) + ')'
	else:
		func_name = func_name + 'sin(x)'


	if b > 0:
		func_name = func_name +  ' + ' + str(b)
	elif b < 0:
		func_name = func_name + ' - ' + str(b * -1)


	os_x = [min(x_points) - 2, max(x_points) + 2]
	os_y = [min(y_points) - 2, max(y_points) + 2]

	plt.plot(os_x, [0, 0], '-b', markersize = 30)
	plt.plot([0, 0], os_y, '-b', markersize = 30)

	plt.plot(x_points, y_points, 'r')

	plt.gca().legend(('x', 'y', 'f(x)'))
	plt.title(func_name)
	plt.axis('equal')
	plt.show()

