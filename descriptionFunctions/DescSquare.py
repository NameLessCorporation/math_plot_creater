
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
	
	if b <= 0:
		x0 = ((-b/k)**2) + a
	else:
		if lang == 'eng':
			x0 = 'Not exist'
		else:
			x0 = 'не существует'

	if lang == 'eng':
		infoString = 'Your args:\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b) + '\n'
		infoString += 'PROPERTIES:\n'

		if k > 0:
			infoString += '1) D(f)=(' + str(a) + '; ∞)\n'
			infoString += '2) E(f)=(' + str(b) + '; ∞)\n'
		else:
			infoString += '1) D(f)=(-∞; ' + str (a) + ')\n'
			infoString += '2) E(f)=(-∞; ' + str (b) + ')\n'

		infoString += 'x0 = ' + str(x0) + '\n'
		infoString += 'General view function\nNon-periodic function\n'

		if k > 0:
			infoString += 'The function increases monotonically on the domain of definition\n'
			infoString += 'Y min = ' + str(min(y_list)) + '    Y max not exist'
		else:
			infoString += 'The function decreases monotonically on the domain of definition.\n'
			infoString += 'Y min not exist   ' + ' Y max = ' + str(min(y_list))
	else:
		infoString = 'Ваши аргументы::\nk= ' + str(k) + '\na= ' + str(a) + '\nb= ' + str(b) + '\n'
		infoString += 'СВОЙСТВА:\n'

		if k > 0:
			infoString += '1) D(f)=(' + str(a) + '; ∞)\n'
			infoString += '2) E(f)=(' + str(b) + '; ∞)\n'
		else:
			infoString += '1) D(f)=(-∞; ' + str (a) + ')\n'
			infoString += '2) E(f)=(-∞; ' + str (b) + ')\n'

		infoString += 'x0 = ' + str(x0) + '\n'
		infoString += 'Функция общего вида\nФункция непериодическая\n'

		if k > 0:
			infoString += 'Функция монотонно возрастает на области определения\n'
			infoString += 'Y мин. = ' + str(min(y_list)) + '    Y макс. не существует'
		else:
			infoString += 'Функция монотонно убывает на области определения.\n'
			infoString += 'Y мин. не существует   ' + ' Y макс. = ' + str(min(y_list))


	label = Label(thirdFrame, text = infoString)
	label.config(font = ('Arial', 15, 'bold'), bg='#1FA7E1', fg='white')
	label.pack()


	#<--Start
	thirdFrame.mainloop()
