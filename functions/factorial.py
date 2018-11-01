
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
from ezprint import *
import matplotlib.pyplot as plt

y_list = []
x_list = []



def create_plot():
	plt.plot(x_list, y_list)

	plt.arrow(0, -1000000, 0, 1000000)
	plt.arrow(-1000000, 0, 1000000, 0)

	plt.gcf().canvas.set_window_title('y=!x')

	plt.grid(color='k', linestyle='-', linewidth=1)

	plt.axis('equal')

	plt.show()


def create_fact(x):
	if x == 0:
		return 1
	return create_fact((x - 1)) * x


def search_points(x, lang):
	global x_list
	global y_list

	for i in np.arange(0, 5):
		x_list.append(i)		
		y = create_fact(i)
		y_list.append(y)
	print('X points: ')
	for i in y_list:
		print(i)
	print('Y points: ')
	for i in x_list:
		print(i)
	create_plot()