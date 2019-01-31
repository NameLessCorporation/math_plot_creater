
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
import numpy as np
import threading

from math import *
from ezprint import *
from tkinter import *
from functions.quadraticTrinomial import *


def main_frame(a, b, c, D, xo, yo, x_null_0, x_null_1, x_null_2, x_list, y_list, lang, func_name):
	global thirdFrame

	infoString = ''

	#<--Settings for secondFrame
	thirdFrame = Tk()

	thirdFrame.title(func_name)

	thirdFrame.resizable(0, 0)

	thirdFrame.config(bg = '#1FA7E1')
	thirdFrame.iconbitmap('docs/favicon.ico')

	def isOdd():
		fx1 = a * 5**2 + b * 5 + c
		fx2 = a * -5**2 + b * -5 + c

		if abs(fx1) == abs(fx2):
			return True
		else:
			return False

	xo = round(xo, 3)

	if isOdd() and lang == 'eng':
		odd = '\nEven function'
	elif isOdd() and lang == 'rus':
		odd = '\nЧетная функция'
	else:
		odd = ''

	#<--Elements
	if lang == 'eng':
		infoString = 'Your args:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c) + '\n' + 'Discriminant: ' + str(D) + '\n' + 'TOPS FUNC.\n' + 'x tops: ' + str(xo) + '\ny tops: ' + str(yo) + '\nNULL FUNC.\n'
		if D == 0:
			infoString += 'x: ' + str(x_null_0) + '\n'
		elif D > 0:
			infoString += 'x1: ' + str(x_null_1) + '\n' + 'x2: ' + str(x_null_2) + '\n'
		else:
			infoString += 'Not exist\n'
		infoString += 'PROPERTIES:\n'
		if a > 0:
			infoString += '1) D(f)=R or (-∞; +∞)\n'
			infoString += '2) E(f)=[' + str(round(min(y_list), 3)) + '; +∞)\n'
			if b == 0:
				infoString += '3) Even function\n'
			else:
				infoString += '3) General view function\n'
			infoString += '4) The function decreases in the interval (-∞; ' + str(xo) + ')\n  The function increases in the interval (' + str(xo) + '; +∞)\n'
			infoString += '5) Asymptote has not\n'
		else:
			infoString += '1) D(f)=R or (-∞; +∞)\n'
			infoString += '2) E(f)=(-∞; ' + str(round(max(y_list), 3)) + ']\n'
			if b == 0:
				infoString += '3) Even function\n'
			else:
				infoString += '3) General view function\n'
			infoString += '4) The function decreases in the interval (' + str(xo) + '; +∞)\n  The function increases in the interval (-∞; ' + str(xo) + ')\n'
			infoString += '5) Asymptote has not\n'
		if a > 0:
			infoString += '6) Min value of x: not exist' + '\n   Min value of y: ' + str(round(min(y_list), 5)) + '\n'
			infoString += '   Max value of x: not exist' + '\n   Max value of y: not exist'
		else:
			infoString += '6) Min value of x: not exist' + '\n   Min value of y: not exist\n'
			infoString += '   Max value of x: not exist' + '\n   Max value of y: ' + str(round(max(y_list), 5))
	else:
		infoString = 'Ваши аргументы:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c) + '\n' + 'Дискриминант: ' + str(D) + '\n' + 'Вершина функции:\n' + 'x tops: ' + str(xo) + '\ny tops: ' + str(yo) + '\nНули функции:\n'
		if D == 0:
			infoString += 'x: ' + str(x_null_0) + '\n'
		elif D > 0:
			infoString += 'x1: ' + str(x_null_1) + '\n' + 'x2: ' + str(x_null_2) + '\n'
		else:
			infoString += 'Не существует\n'
		infoString += 'СВОЙСТВА:\n'
		if a > 0:
			infoString += '1) D(f)=R or (-∞; +∞)\n'
			infoString += '2) E(f)=[' + str(round(min(y_list), 3)) + '; +∞)\n'
			if b == 0:
				infoString += '3) Четная функция\n'
			else:
				infoString += '3) Функция общего вида\n'
			infoString += '4) Функция уменьшается в интервале (-∞; ' + str(xo) + ')\n  Функция увеличивается в интервале (' + str(xo) + '; +∞)'
			infoString += '5) Нет асимптоты\n'
		else:
			infoString += '1) D(f)=R or (-∞; +∞)\n'
			infoString += '2) E(f)=(-∞; ' + str(round(max(y_list), 3)) + ']\n'
			if b == 0:
				infoString += '3) Четная функция\n'
			else:
				infoString += '3) Функция общего вида\n'
			infoString += '4)Ф ункция уменьшается в интервале (' + str(xo) + '; +∞)\n  Функция увеличивается в интервале (-∞; ' + str(xo) + ')\n'
			infoString += '5) Нет асимптоты\n'
		if a > 0:
			infoString += '6) Мин. значение X: не существует' + '\n   Мин. значение Y:' + str(round(min(y_list), 5)) + '\n'
			infoString += '   Макс. значение X: не существует' + '\n   Макс. значение Y: не существует'
		else:
			infoString += '6) Мин. значение X: не существует' + '\n   Мин. значение Y: не существует'
			infoString += '   Макс. значение X: не существует' + '\n   Макс. значение Y: ' + str(round(max(y_list), 5))

	label = Label(thirdFrame, text = infoString)
	label.config(font = ('Arial', 15, 'bold'), bg='#1FA7E1', fg='white')
	label.pack()


	#<--Start
	thirdFrame.mainloop()