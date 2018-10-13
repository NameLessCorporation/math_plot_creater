
#<--Import lib
import math
import decimal
import numpy as np
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt


def creat_hyperbola(k, a, b):
	x_points = []
	y_points = []

	x_points = np.around(np.arange(-10, 10, 0.1), decimals=4)
	y_points = (k / x_points - a) + b

	plt.plot(x_points, y_points)
	plt.axis('equal')
	plt.show()