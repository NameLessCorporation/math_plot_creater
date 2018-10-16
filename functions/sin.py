
import math
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def creat_sin(k, a, b):
	x_points = []
	y_points = []

	x_points = np.arange(-10.0, 10.0, 0.1)
	new_x  = []
	for i in range(len(x_points)):
		new_x.append(x_points[i] - 5)
		y = k * (math.sin(x_points[i])) + b
		y_points.append(y)
	x_points = new_x

	plt.plot(x_points, y_points)
	plt.axis('equal')
	plt.show()

