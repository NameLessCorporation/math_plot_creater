
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
from ezprint import *
from tkinter import *
import numpy as np
import decimal
#<--Import functions with file-->
from functions.sin import *
from functions.cos import *
from functions.cubic import *
from functions.linear import *
from functions.square import *
from functions.quadratic import *
from functions.hyperbola import *
from functions.quadraticTrinomial import *

firstFrame = None
secondFrame = None

firstFrameElements = []

v = None
k = None
a = None
b = None
c = None

lang = 'eng'


def set_eng():
	global firstFrameElements
	global firstFrame
	global lang

	lang = 'eng'

	firstFrameElements[0].config(text = 'CHOOSE PLOT:')

	firstFrameElements[1].config(text = 'Linear function')
	firstFrameElements[2].config(text = 'Quadratic function')
	firstFrameElements[3].config(text = 'Cubic function')
	firstFrameElements[4].config(text = 'Hyperbola function')
	firstFrameElements[5].config(text = 'Square function')
	firstFrameElements[6].config(text = 'Sine function')
	firstFrameElements[7].config(text = 'Cosine function')
	firstFrameElements[8].config(text = 'Quadratic trinomial')

	firstFrameElements[9].config(text = 'DRAW FUNCTION')


def set_rus():
	global firstFrameElements
	global firstFrame
	global lang

	lang = 'rus'

	firstFrameElements[0].config(text = 'ВЫБЕРИТЕ ГРАФИК:')

	firstFrameElements[1].config(text = 'Линейная функция')
	firstFrameElements[2].config(text = 'Квадратичния функция')
	firstFrameElements[3].config(text = 'Кубическая функция')
	firstFrameElements[4].config(text = 'Обратная пропорциональность')
	firstFrameElements[5].config(text = 'Корневая функция')
	firstFrameElements[6].config(text = 'Функция синуса')
	firstFrameElements[7].config(text = 'Функция косинуса')
	firstFrameElements[8].config(text = 'Квадратный трёхчлен')

	firstFrameElements[9].config(text = 'НАЧЕРТИТЬ ФУНКЦИЮ')



def draw():
	global k
	global a
	global b

	if v.get() == 1:
		create_linear(float(k), float(a), float(b))
	elif v.get() == 2:
		create_quadratic(float(k), float(a), float(b))
	elif v.get() == 3:
		create_cubic(float(k), float(a), float(b))
	elif v.get() == 4:
		create_hyperbola(float(k), float(a), float(b))
	elif v.get() == 5:
		create_square(float(k), float(a), float(b))
	elif v.get() == 6:
		create_sin(float(k), float(a), float(b))
	elif v.get() == 7:
		create_cos(float(k), float(a), float(b))
	elif v.get() == 8:
		create_qt(float(k), float(a), float(b))


def creat_plot():
	global secondFrame
	global v
	global k
	global a
	global b

	k = k.get()
	a = a.get()
	b = b.get()
	secondFrame.destroy()
	draw()
	

def input_arg(v):
	global firstFrame
	global secondFrame
	global k
	global a
	global b
	#<--Settings for secondFrame
	firstFrame.destroy()
	secondFrame = Tk()

	secondFrame.title('PLOT_CREATER')

	secondFrame.resizable(0, 0)

	secondFrame.config(bg = '#1FA7E1')
	secondFrame.config()
	#<--Elements
	if v.get() == 8:
		label1 = Label(secondFrame, text = 'Input a:', bg='#1FA7E1', fg='white')

		k = Entry(secondFrame, width = 20)

		label2 = Label(secondFrame, text = 'Input b:', bg='#1FA7E1', fg='white')

		a = Entry(secondFrame, width = 20)

		label3 = Label(secondFrame, text = 'Input c:', bg='#1FA7E1', fg='white')

		b = Entry(secondFrame, width = 20)
	else:
		label1 = Label(secondFrame, text = 'Input k:', bg='#1FA7E1', fg='white')

		k = Entry(secondFrame, width = 20)

		label2 = Label(secondFrame, text = 'Input a:', bg='#1FA7E1', fg='white')

		a = Entry(secondFrame, width = 20)

		label3 = Label(secondFrame, text = 'Input b:', bg='#1FA7E1', fg='white')

		b = Entry(secondFrame, width = 20)

	button = Button(secondFrame, text = 'Draw', command = creat_plot)

	k.delete(0, END)
	k.insert(0, '1')

	a.delete(0, END)
	a.insert(0, '0')

	b.delete(0, END)
	b.insert(0, '0')

	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))

	k.config(font = ('Arial', 15, 'bold'))

	label2.config(font = ('Arial', 15, 'bold'))

	a.config(font = ('Arial', 15, 'bold'))

	label3.config(font = ('Arial', 15, 'bold'))

	b.config(font = ('Arial', 15, 'bold'))

	button.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 1)

	k.grid(column = 0, row = 2)

	label2.grid(column = 0, row = 3)

	a.grid(column = 0, row = 4)

	label3.grid(column = 0, row = 5)

	b.grid(column = 0, row = 6)

	button.grid(column = 0, columnspan = 7)

	#<--Start
	secondFrame.mainloop()


def mainFrame():
	global firstFrameElements
	global firstFrame
	global v
	#<--Settings for firstFrame
	firstFrame = Tk()

	firstFrame.title('PLOT_CREATER')

	firstFrame.resizable(0, 0)

	firstFrame.config(bg = '#1FA7E1')
	firstFrame.config()

	v = IntVar()
	#<--Elements
	label = Label(firstFrame, text = 'CHOOSE PLOT:', bg='#1FA7E1', fg='white')
	firstFrameElements.append(label)

	radio1 = Radiobutton(firstFrame, text="Linear function", variable=v, value=1)
	radio2 = Radiobutton(firstFrame, text="Quadratic function", variable=v, value=2)
	radio3 = Radiobutton(firstFrame, text="Cubic function", variable=v, value=3)
	radio4 = Radiobutton(firstFrame, text="Hyperbola function", variable=v, value=4)
	radio5 = Radiobutton(firstFrame, text="Square function", variable=v, value=5)
	radio6 = Radiobutton(firstFrame, text="Sine function", variable=v, value=6)
	radio7 = Radiobutton(firstFrame, text="Cosine function", variable=v, value=7)
	radio8 = Radiobutton(firstFrame, text="Quadratic trinomial", variable=v, value=8)

	firstFrameElements.append(radio1)
	firstFrameElements.append(radio2)
	firstFrameElements.append(radio3)
	firstFrameElements.append(radio4)
	firstFrameElements.append(radio5)
	firstFrameElements.append(radio6)
	firstFrameElements.append(radio7)
	firstFrameElements.append(radio8)

	button = Button(firstFrame, text = 'DRAW FUNCTION', command = lambda: input_arg(v))

	firstFrameElements.append(button)
	#<--Configs
	label.config(font = ('Arial', 15, 'bold'))

	radio1.config(bg = '#1FA7E1')
	radio2.config(bg = '#1FA7E1')
	radio3.config(bg = '#1FA7E1')
	radio4.config(bg = '#1FA7E1')
	radio5.config(bg = '#1FA7E1')
	radio6.config(bg = '#1FA7E1')
	radio7.config(bg = '#1FA7E1')
	radio8.config(bg = '#1FA7E1')

	radio1.select()

	button.config(font = ('Arial', 15, 'bold'))
	#<--Grids
	label.grid(column = 0, row = 0)

	radio1.grid(column = 0, row = 1)
	radio2.grid(column = 0, row = 2)
	radio3.grid(column = 0, row = 3)
	radio4.grid(column = 0, row = 4)
	radio5.grid(column = 0, row = 5)
	radio6.grid(column = 0, row = 6)
	radio7.grid(column = 0, row = 7)
	radio8.grid(column = 0, row = 8)

	button.grid(column = 0, columnspan = 2)

	main_menu = Menu(firstFrame)
	firstFrame.config(menu = main_menu)
	lang_menu = Menu(main_menu)
	main_menu.add_cascade(label="Language", menu = lang_menu)
	lang_menu.add_command(label="English", command = set_eng)
	lang_menu.add_command(label="Russian", command = set_rus)
	#<--Start
	firstFrame.mainloop()


if __name__ == '__main__':
	mainFrame()