
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
from ezprint import *
from tkinter import *

bg = '#10355B'
fg = '#DDDFD2'

def info(lang):
	#<--Settings for secondFrame
	fourthFrame = Tk()

	fourthFrame.title('Info')

	fourthFrame.resizable(0, 0)

	fourthFrame.config(bg = bg)
	fourthFrame.iconbitmap('docs/favicon.ico')

	# print(lang)

	#<--Elements
	if lang == 'eng':
		label2 = Label(fourthFrame, text = 'Linear function - y=k*(x-a)+b', bg=bg, fg=fg)
		label3 = Label(fourthFrame, text = 'Quadratic function - y=k*(x-a)^2+b', bg=bg, fg=fg)
		label4 = Label(fourthFrame, text = 'Square function - y=k*sqrt(x-a)+b', bg=bg, fg=fg)
		label5 = Label(fourthFrame, text = 'Cubic function - y=k*(x-a)^3+b', bg=bg, fg=fg)
		label6 = Label(fourthFrame, text = 'Hyperbola function - y=k/(x-a)+b', bg=bg, fg=fg)
		label7 = Label(fourthFrame, text = 'Sine function - y=k*sin(x-a)+b', bg=bg, fg=fg)
		label8 = Label(fourthFrame, text = 'Cosine function - y=k*cos(x-a)+b', bg=bg, fg=fg)
		label9 = Label(fourthFrame, text = 'QuadraticTrinomial - y=ax^2+bx+c', bg=bg, fg=fg)
		label10 = Label(fourthFrame, text = 'Factorial function - y=!x', bg=bg, fg=fg)
		label11 = Label(fourthFrame, text = '|Linear| function - y=k*|x-a|+b', bg=bg, fg=fg)
	else:
		label2 = Label(fourthFrame, text = 'Линейная функция - y=k*(x-a)+b', bg=bg, fg=fg)
		label3 = Label(fourthFrame, text = 'Квадратичния функция - y=k*(x-a)^2+b', bg=bg, fg=fg)
		label4 = Label(fourthFrame, text = 'Кубическая функция - y=k*sqrt(x-a)+b', bg=bg, fg=fg)
		label5 = Label(fourthFrame, text = 'Обратная пропорциональность - y=k*(x-a)^3+b', bg=bg, fg=fg)
		label6 = Label(fourthFrame, text = 'Корневая функция - y=k/(x-a)+b', bg=bg, fg=fg)
		label7 = Label(fourthFrame, text = 'Функция синуса - y=k*sin(x-a)+b', bg=bg, fg=fg)
		label8 = Label(fourthFrame, text = 'Функция косинуса - y=k*cos(x-a)+b', bg=bg, fg=fg)
		label9 = Label(fourthFrame, text = 'Квадратный трёхчлен - y=ax^2+bx+c', bg=bg, fg=fg)
		label10 = Label(fourthFrame, text = 'Функция факториал - y=!x', bg=bg, fg=fg)
		label11 = Label(fourthFrame, text = '|Линейная| функция - y=k*|x-a|+b', bg=bg, fg=fg)

	#<--Configs
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
	label2.grid(column = 0, row = 0)
	label3.grid(column = 0, row = 1)
	label4.grid(column = 0, row = 2)
	label5.grid(column = 0, row = 3)
	label6.grid(column = 0, row = 4)
	label7.grid(column = 0, row = 5)
	label8.grid(column = 0, row = 6)
	label9.grid(column = 0, row = 7)
	label10.grid(column = 0, row = 8)
	label11.grid(column = 0, row = 9)


	#<--Start
	fourthFrame.mainloop()