
import matplotlib.pyplot as plt
import numpy as np
import threading

from math import *
from ezprint import *
from tkinter import *


def main_frame(k, a, b, x_list, y_list, lang, func_name):
	global thirdFrame

	infoString = ''

	#<--Settings for secondFrame
	thirdFrame = Tk()

	thirdFrame.title(func_name)

	thirdFrame.resizable(0, 0)

	thirdFrame.config(bg = '#1FA7E1')
	thirdFrame.iconbitmap('docs/favicon.ico')

	if lang == 'eng':
		infoString = 'Your args:\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b) + '\n'
		infoString += 'PROPERTIES:\n'

		infoString += '1) D(f)=(-∞; ' + str(a) + ')U(' + str(a) + '; +∞)\n'
		infoString += '2) E(f)=(-∞; ' + str(b) + ')U(' + str(b) + '; +∞)\n'
		
		if a == 0 and b == 0:
			infoString += 'The function is odd\n'
		else:
			infoString += 'General view function\n'

		infoString += 'Asymptotes: x = ' + str(a) + '   y = ' + str(b) + '\n'

		if k > 0:
			infoString += 'The function on each of the intervals (-∞; ' + str(a) + ')U(' + str(a) + '; +∞) is decreasing.\n'
		else:
			infoString += 'The function on each of the intervals (-∞; ' + str(a) + ')U(' + str(a) + '; +∞) is increasing.\n'
			# infoString += 'The function takes negative values on the interval and takes positive values on the interval'

		infoString += 'The function does not have the smallest and largest values.\n'
	else:
		infoString = 'Ваши аргументы:\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b) + '\n'
		infoString += 'СВОЙСТВА:\n'

		infoString += '1) D(f)=(-∞; ' + str(a) + ')U(' + str(a) + '; +∞)\n'
		infoString += '2) E(f)=(-∞; ' + str(b) + ')U(' + str(b) + '; +∞)\n'
		
		if a == 0 and b == 0:
			infoString += 'Нечетная функция\n'
		else:
			infoString += 'Функция общего вида\n'

		infoString += 'Асимптоты: x = ' + str(a) + '   y = ' + str(b) + '\n'

		if k > 0:
			infoString += 'Функция на каждом из промежутков (-∞; ' + str(a) + ')U(' + str(a) + '; +∞) является убывающей.\n'
		else:
			infoString += 'Функция на каждом из промежутков (-∞; ' + str(a) + ')U(' + str(a) + '; +∞) является возрастающей.\n'
			# infoString += 'The function takes negative values on the interval and takes positive values on the interval'

		infoString += 'Функция не имеет наименьших и наибольших значений.\n'


	label = Label(thirdFrame, text = infoString)
	label.config(font = ('Arial', 15, 'bold'), bg='#1FA7E1', fg='white')
	label.pack()


	#<--Start
	thirdFrame.mainloop()
