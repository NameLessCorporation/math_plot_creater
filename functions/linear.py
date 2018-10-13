
#<--Import lib
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def creat_linear(k, a, b):
	x_points = []
	y_points = []

	for x in range(-10, 11):
		x_points.append(x - a)
		y = k * x + b
		y_points.append(y)

	plt.plot(x_points, y_points)
	plt.axis('equal')
	plt.show()

