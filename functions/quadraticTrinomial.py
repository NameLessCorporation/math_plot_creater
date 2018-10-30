
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
from math import *
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt

x_list = x_points = np.arange(-5.0, 5.0, 0.1)
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


def main():
	try:
		a = int(input('Input a: '))
	except:
		a = 1
	try:
		b = int(input('Input b: '))
	except:
		b = 1
	try:
		c = int(input('Input c: '))
	except:
		c = 1
	f(a, b, c)
	cls()
	create_qt(a, b, c)
	p('Your args:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c))
	p('Discriminant: ' + str(D))
	p('TOPS FUNC.')
	p('x tops: ' + str(xo))
	p('y tops: ' + str(yo))
	p('NULL FUNC.')
	p('x_0 null: ' + str(x_null_0))
	p('x_1 null: ' + str(x_null_1))
	p('x_2 null: ' + str(x_null_2))
	p('PROPERTIES:')
	p('1) D(f)=R or (-∞; +∞)\n2) E(f)=[0; +∞)\n3) Even function\n4)The function decreases in the interval (-∞; 0)\n  The function increases in the interval (0; +∞)\n5) Asymptote has not')
	p('6) Min value of x: ' + str(round(np.amin(x_list), 5)) + '\n   Min value of y: ' + str(round(min(y_list), 5)))
	p('   Max value of x: ' + str(round(np.amax(x_list), 5)) + '\n   Max value of y: ' + str(round(max(y_list), 5)))