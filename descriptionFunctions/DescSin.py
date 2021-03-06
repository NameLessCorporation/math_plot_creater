
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
import numpy as np
import threading

from math import *
from ezprint import *
from tkinter import *

def main_frame(a, b, c, xo, yo, x_list, y_list, lang, func_name):
	global thirdFrame

	#<--Settings for secondFrame
	thirdFrame = Tk()

	thirdFrame.title(func_name)

	thirdFrame.resizable(0, 0)

	thirdFrame.config(bg = '#1FA7E1')
	thirdFrame.iconbitmap('docs/favicon.ico')

	xo = round(xo, 3)

	if a == 0:
		even = True
	else:
		even = False

	#<--Elements
	if lang == 'eng':
		label1 = Label(thirdFrame, text = 'Your args:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c), bg='#1FA7E1', fg='white')
		label2 = Label(thirdFrame, text = 'TOPS FUNC.', bg='#1FA7E1', fg='white')
		label3 = Label(thirdFrame, text = 'x tops: ' + str(xo), bg='#1FA7E1', fg='white')
		label4 = Label(thirdFrame, text = 'y tops: ' + str(yo), bg='#1FA7E1', fg='white')
		label5 = Label(thirdFrame, text = 'PROPERTIES:', bg='#1FA7E1', fg='white')
		if even:
			label9 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=[' + str(min(y_list)) + '; ' + str(max(y_list)) + ']\n3) Even function\n4)The function decreases in the interval (-∞; ' + str(xo) + ')\n  The function increases in the interval (' + str(xo) + '; +∞)\n5) Asymptote has not', bg='#1FA7E1', fg='white')
		else:
			label9 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=[' + str(min(y_list)) + '; ' + str(max(y_list) + ']\n3) Even function\n4)The function decreases in the interval (-∞; ' + str(xo) + ')\n  The function increases in the interval (' + str(xo) + '; +∞)\n5) Asymptote has not', bg='#1FA7E1', fg='white')
	else:
		label1 = Label(thirdFrame, text = 'Ваши аргументы:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c), bg='#1FA7E1', fg='white')
		label2 = Label(thirdFrame, text = 'Дискриминант: ' + str(D), bg='#1FA7E1', fg='white')
		label3 = Label(thirdFrame, text = 'Вершина функции:', bg='#1FA7E1', fg='white')
		label4 = Label(thirdFrame, text = 'x: ' + str(xo), bg='#1FA7E1', fg='white')
		label5 = Label(thirdFrame, text = 'y: ' + str(yo), bg='#1FA7E1', fg='white')
		label6 = Label(thirdFrame, text = 'Нули функции:', bg='#1FA7E1', fg='white')
		if D == 0:
			label7 = Label(thirdFrame, text = 'x: ' + str(x_null_0), bg='#1FA7E1', fg='white')
		elif D > 0:
			label7 = Label(thirdFrame, text = 'x1: ' + str(x_null_1) + '\n' + 'x2: ' + str(x_null_2), bg='#1FA7E1', fg='white')
		else:
			label7 = Label(thirdFrame, text = 'Не существует', bg='#1FA7E1', fg='white')
		label8 = Label(thirdFrame, text = 'СВОЙСТВА:', bg='#1FA7E1', fg='white')
		if a > 0:
			label9 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=[0; +∞)\n3) Четная функция\n4)Функция уменьшается в интервале (-∞; ' + str(xo) + ')\n  Функция уменьшается в интервале (' + str(xo) + '; +∞)\n5) Нет асимптоты', bg='#1FA7E1', fg='white')
		else:
			label9 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=(-∞; 0]\n3) Четная функция\n4)Функция уменьшается в интервале (' + str(xo) + '; +∞)\n  Функция уменьшается в интервале (-∞; ' + str(xo) + ')\n5) Нет асимптоты', bg='#1FA7E1', fg='white')
		if a > 0:
			label10 = Label(thirdFrame, text = '6) Мин. значение X: не существует' + '\n   Мин. значение Y:' + str(round(min(y_list), 5)), bg='#1FA7E1', fg='white')
			label11 = Label(thirdFrame, text = '   Макс. значение X: не существует' + '\n   Макс. значение Y: не существует', bg='#1FA7E1', fg='white')
		else:
			label10 = Label(thirdFrame, text = '6) Мин. значение X: не существует' + '\n   Мин. значение Y: не существует', bg='#1FA7E1', fg='white')
			label11 = Label(thirdFrame, text = '   Макс. значение X: не существует' + '\n   Макс. значение Y: ' + str(round(max(y_list), 5)), bg='#1FA7E1', fg='white')

	
	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))
	label2.config(font = ('Arial', 15, 'bold'))
	label3.config(font = ('Arial', 15, 'bold'))
	label4.config(font = ('Arial', 15, 'bold'))
	label5.config(font = ('Arial', 15, 'bold'))
	label6.config(font = ('Arial', 15, 'bold'))
	label7.config(font = ('Arial', 15, 'bold'))
	label8.config(font = ('Arial', 15, 'bold'))
	label9.config(font = ('Arial', 15, 'bold'))
	label10.config(font = ('Arial', 15, 'bold'))
	label11.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)
	label3.grid(column = 0, row = 2)
	label4.grid(column = 0, row = 3)
	label5.grid(column = 0, row = 4)
	label6.grid(column = 0, row = 5)
	label7.grid(column = 0, row = 6)
	label8.grid(column = 0, row = 7)
	label9.grid(column = 0, row = 8)
	label10.grid(column = 0, row = 9)
	label11.grid(column = 0, row = 10)

	#<--Start
	thirdFrame.mainloop()