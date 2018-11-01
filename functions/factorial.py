
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
from ezprint import *
import matplotlib.pyplot as plt

y_list = []
x_list = []


def create_plot(x):
	plt.plot(x_list, y_list, 'r')

	plt.arrow(0, -1000000, 0, 2000000)
	plt.arrow(-1000000, 0, 2000000, 0)

	plt.gcf().canvas.set_window_title('y=!' + str(x))

	plt.grid(color='k', linestyle='-', linewidth=0.5)

	plt.axis('equal')

	plt.show()


def create_fact(x):
	if x == 0:
		return 1
	return create_fact((x - 1)) * x


def search_points(x, lang):
	global x_list
	global y_list

	for i in np.arange(0, x):
		x_list.append(i)		
		y = create_fact(i)
		y_list.append(y)
	create_plot(x)