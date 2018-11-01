
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
import numpy as np
import threading

from math import *
from ezprint import *
from tkinter import *


def desc(k, a, b, lang, func_name):
	thirdFrame = Tk()

	thirdFrame.title(func_name)

	thirdFrame.resizable(0, 0)

	thirdFrame.config(bg = '#1FA7E1')
	thirdFrame.iconbitmap('docs/favicon.ico')

	x0 = round(-b/k, 3)

	if lang == 'eng':
		label1 = Label(thirdFrame, text = 'Your args:\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b), bg='#1FA7E1', fg='white')
		label2 = Label(thirdFrame, text = 'D(f)=R or (-∞; +∞)', bg='#1FA7E1', fg='white')
		label3 = Label(thirdFrame, text = 'E(f)=R or (-∞; +∞)', bg='#1FA7E1', fg='white')
		label4 = Label(thirdFrame, text = 'NULL FUNC.: ' + str(x0), bg='#1FA7E1', fg='white')
		if k > 0:
			label5 = Label(thirdFrame, text = 'The function monotonically increases', bg='#1FA7E1', fg='white')
			label6 = Label(thirdFrame, text = 'The function takes negative values on the interval (-∞; ' + str(x0) + ')\nPositive values on the interval (' + str(x0) + '; +∞)' , bg='#1FA7E1', fg='white')
		else:
			label5 = Label(thirdFrame, text = 'The function monotonically decreasing', bg='#1FA7E1', fg='white')
			label6 = Label(thirdFrame, text = 'The function takes negative values on the interval (' + str(x0) + '; +∞)\nPositive values on the interval (-∞; ' + str(x0) + ')' , bg='#1FA7E1', fg='white')
		label7 = Label(thirdFrame, text = 'Function odd' , bg='#1FA7E1', fg='white')
	else:
		label1 = Label(thirdFrame, text = 'Ваши аргументы:\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b), bg='#1FA7E1', fg='white')
		label2 = Label(thirdFrame, text = 'D(f)=R or (-∞; +∞)', bg='#1FA7E1', fg='white')
		label3 = Label(thirdFrame, text = 'E(f)=R or (-∞; +∞)', bg='#1FA7E1', fg='white')
		label4 = Label(thirdFrame, text = 'Нуль функции: ' + str(x0), bg='#1FA7E1', fg='white')
		if k > 0:
			label5 = Label(thirdFrame, text = 'Функция монотонно возрастает', bg='#1FA7E1', fg='white')
			label6 = Label(thirdFrame, text = 'Функция принимает отрицательные значения на промежутке (-∞; ' + str(x0) + ')\nПоложительные значения на промежутке (' + str(x0) + '; +∞)' , bg='#1FA7E1', fg='white')
		else:
			label5 = Label(thirdFrame, text = 'Функция монотонно убывает', bg='#1FA7E1', fg='white')
			label6 = Label(thirdFrame, text = 'Функция принимает отрицательные значения на промежутке (' + str(x0) + '; +∞)\nПоложительные значения на промежутке (-∞; ' + str(x0) + ')' , bg='#1FA7E1', fg='white')
		label7 = Label(thirdFrame, text = 'Функция нечетная' , bg='#1FA7E1', fg='white')

	label1.config(font = ('Arial', 15, 'bold'))
	label2.config(font = ('Arial', 15, 'bold'))
	label3.config(font = ('Arial', 15, 'bold'))
	label4.config(font = ('Arial', 15, 'bold'))
	label5.config(font = ('Arial', 15, 'bold'))
	label6.config(font = ('Arial', 15, 'bold'))
	label7.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)
	label3.grid(column = 0, row = 2)
	label4.grid(column = 0, row = 3)
	label5.grid(column = 0, row = 4)
	label6.grid(column = 0, row = 5)
	label7.grid(column = 0, row = 6)

	thirdFrame.mainloop()