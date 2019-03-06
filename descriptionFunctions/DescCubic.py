
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
import numpy as np
import threading

from math import *
from ezprint import *
from tkinter import *
from functions.cubic import *


bg = '#10355B'
fg = '#DDDFD2'


def main_frame(k, a, b, x_list, y_list, lang, func_name):
	global thirdFrame

	infoString = ''

	#<--Settings for secondFrame
	thirdFrame = Tk()

	thirdFrame.title(func_name)

	thirdFrame.resizable(0, 0)

	thirdFrame.config(bg = '#1FA7E1')
	thirdFrame.iconbitmap('docs/favicon.ico')

	# print(np.roots([k]))
	# print(x_list[y_list.index(0)])

	# if -b/k > 0:
	# 	x0 = pow(-b/k , float(1)/3) + a
	# elif -b/k < 0:
	# 	x0 = -pow(abs(b/k) , float(1)/3) + a
	# else:
	# 	x0 = 0

	c = (-b/k)**(1/3)
	x0 = (a + c.real)
	print(x0)
	print(c.real)
	# print(type((-b/k)**(1/3)))

	def isOdd():
		if a == 0 and b == 0:
			return True
		return False

	if lang == 'eng':
		infoString = 'Your args:\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b) + '\n'
		# infoString +=  '\nNULL FUNC: \nx0: ' + str(x0) + '\n'

		infoString += 'PROPERTIES:\n'

		infoString += '1) D(f)=R or (-∞; +∞)\n'
		infoString += '2) E(f)=R or (-∞; +∞)\n'

		if isOdd():
			infoString += '3) Even function\n'
		else:
			infoString += '3) General view function\n'

		if a > 0:
			infoString += '4) The function increases in the interval (-∞; +∞)\n'
		else:
			infoString += '4) The function decreases in the interval (-∞; +∞)\n'

		infoString += '5) Asymptote has not\n'

		infoString += '6) Min value of x: not exist' + '\n   Min value of y: not exist\n'
		infoString += '   Max value of x: not exist' + '\n   Max value of y: not exist'
	else:
		infoString = 'Ваши аргументы::\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b) + '\n'
		# infoString +=  '\nНоль функции: \nx0: ' + str(x0) + '\n'
		infoString += 'СВОЙСТВА:\n'

		infoString += '1) D(f)=R or (-∞; +∞)\n'
		infoString += '2) E(f)=R or (-∞; +∞)\n'

		if isOdd():
			infoString += '3) Нечетная функция\n'
		else:
			infoString += '3) Функция общего вида\n'

		if a > 0:
			infoString += '4) Функция увеличивается в интервале (-∞; +∞)\n'
		else:
			infoString += '4) Функция уменьшается в интервале (-∞; +∞)\n'

		infoString += '5) Нет асимптоты\n'

		infoString += '6) Мин. значение X: не существует' + '\n   Мин. значение Y: не существует\n'
		infoString += '   Макс. значение X: не существует' + '\n   Макс. значение Y: не существует'


	label = Label(thirdFrame, text = infoString)
	label.config(font = ('Arial', 15, 'bold'), bg=bg, fg=fg)
	label.pack()

	#<--Start
	thirdFrame.mainloop()