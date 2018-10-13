
#<--Import lib
import math
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def creat_cubic(k, a, b):
	x_points = []
	y_points = []

	x_points = np.arange(-1.5, 1.5, 0.1)
	new_x  = []
	for i in range(len(x_points)):
		new_x.append(x_points[i])
		y = k * ((x_points[i] - a) ** 3) + b
		y_points.append(y)
	x_points = new_x

	plt.plot(x_points, y_points)
	plt.axis('equal')
	plt.show()