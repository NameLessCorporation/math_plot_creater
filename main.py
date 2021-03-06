
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
from ezprint import *
from tkinter import *
import numpy as np
import decimal
#<--Import functions with file-->
from help.info import *
from help.authors import *
from functions.sin import *
from functions.cos import *
from functions.cubic import *
from functions.linear import *
from functions.square import *
from functions.factorial import *
from functions.quadratic import *
from functions.hyperbola import *
from functions.linearModule import *
from functions.quadraticTrinomial import *

firstFrame = None
secondFrame = None

firstFrameElements = []

v = None
k = None
a = None
b = None
c = None
nk = None
na = None
nb = None
nc = None

lang = 'eng'


def set_eng():
	global firstFrameElements
	global firstFrame
	global lang

	if lang != 'eng':
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
		firstFrameElements[9].config(text = 'Factorial function')
		firstFrameElements[10].config(text = '|Linear| function')

		firstFrameElements[11].config(text = 'DRAW FUNCTION')


def set_rus():
	global firstFrameElements
	global firstFrame
	global lang

	if lang != 'rus':
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
		firstFrameElements[9].config(text = 'Функция факториал')
		firstFrameElements[10].config(text = '|Линейная| функция')

		firstFrameElements[11].config(text = 'НАЧЕРТИТЬ ГРАФИК')


def draw():
	global nk
	global na
	global nb

	if v.get() == 1:
		create_linear(float(nk), float(na), float(nb), lang)
	elif v.get() == 2:
		create_quadratic(float(nk), float(na), float(nb))
	elif v.get() == 3:
		create_cubic(float(nk), float(na), float(nb), lang)
	elif v.get() == 4:
		create_hyperbola(float(nk), float(na), float(nb), lang)
	elif v.get() == 5:
		create_square(float(nk), float(na), float(nb), lang)
	elif v.get() == 6:
		create_sin(float(nk), float(na), float(nb))
	elif v.get() == 7:
		create_cos(float(nk), float(na), float(nb))
	elif v.get() == 8:
		create_qt(float(nk), float(na), float(nb), lang)
	elif v.get() == 9:
		search_points(int(nk), lang)
	elif v.get() == 10:
		create_linear_with_module(float(nk), float(na), float(nb), lang)


def creat_plot():
	global secondFrame
	global v
	global k
	global a
	global b
	global nk
	global na
	global nb

	nk = k.get()
	if v.get() != 9:
		na = a.get()
		nb = b.get()
	if float(nk) != 0:
		secondFrame.destroy()
		draw()
	

def input_arg(v, lang):
	global firstFrame
	global secondFrame
	global k
	global a
	global b

	bg = '#10355B'
	fg = '#DDDFD2'
	#<--Settings for secondFrame
	firstFrame.destroy()
	secondFrame = Tk()

	secondFrame.title('PLOT_CREATER')

	secondFrame.resizable(0, 0)

	secondFrame.config(bg = bg)
	secondFrame.iconbitmap('docs/favicon.ico')
	widthLabel = 15
	
	#<--Elements
	if lang == 'eng':
		if v.get() == 8:
			label1 = Label(secondFrame, text = 'Input a:', bg=bg, fg=fg)

			k = Entry(secondFrame, width = widthLabel)

			label2 = Label(secondFrame, text = 'Input b:', bg=bg, fg=fg)

			a = Entry(secondFrame, width = widthLabel)

			label3 = Label(secondFrame, text = 'Input c:', bg=bg, fg=fg)

			b = Entry(secondFrame, width = widthLabel)
		elif v.get() == 9:
			label1 = Label(secondFrame, text = 'Input x:', bg=bg, fg=fg)

			k = Entry(secondFrame, width = widthLabel)
		else:
			label1 = Label(secondFrame, text = 'Input k:', bg=bg, fg=fg)

			k = Entry(secondFrame, width = widthLabel)

			label2 = Label(secondFrame, text = 'Input a:', bg=bg, fg=fg)

			a = Entry(secondFrame, width = widthLabel)

			label3 = Label(secondFrame, text = 'Input b:', bg=bg, fg=fg)

			b = Entry(secondFrame, width = widthLabel)

		button = Button(secondFrame, text = 'DRAW', command = creat_plot)
	else:
		if v.get() == 8:
			label1 = Label(secondFrame, text = 'Введите a:', bg=bg, fg=fg)

			k = Entry(secondFrame, width = widthLabel)

			label2 = Label(secondFrame, text = 'Введите b:', bg=bg, fg=fg)

			a = Entry(secondFrame, width = widthLabel)

			label3 = Label(secondFrame, text = 'Введите c:', bg=bg, fg=fg)

			b = Entry(secondFrame, width = widthLabel)
		elif v.get() == 9:
			label1 = Label(secondFrame, text = 'Введите x:', bg=bg, fg=fg)

			k = Entry(secondFrame, width = widthLabel)
		else:
			label1 = Label(secondFrame, text = 'Введите k:', bg=bg, fg=fg)

			k = Entry(secondFrame, width = widthLabel)

			label2 = Label(secondFrame, text = 'Введите a:', bg=bg, fg=fg)

			a = Entry(secondFrame, width = widthLabel)

			label3 = Label(secondFrame, text = 'Введите b:', bg=bg, fg=fg)

			b = Entry(secondFrame, width = widthLabel)

		button = Button(secondFrame, text = 'НАЧЕРТИТЬ', command = creat_plot)

	k.delete(0, END)
	k.insert(0, '1')
	if v.get() != 9:
		a.delete(0, END)
		a.insert(0, '0')

		b.delete(0, END)
		b.insert(0, '0')

	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))

	k.config(font = ('Arial', 15, 'bold'))
	if v.get() != 9:
		label2.config(font = ('Arial', 15, 'bold'))

		a.config(font = ('Arial', 15, 'bold'))

		label3.config(font = ('Arial', 15, 'bold'))

		b.config(font = ('Arial', 15, 'bold'))

	button.config(font = ('Arial', 12, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 1)

	k.grid(column = 0, row = 2)
	if v.get() != 9:
		label2.grid(column = 0, row = 3)

		a.grid(column = 0, row = 4)

		label3.grid(column = 0, row = 5)

		b.grid(column = 0, row = 6)

	button.grid(column = 0, columnspan = 7, pady = 5)

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

	bg = '#10355B'
	fg = '#DDDFD2'

	firstFrame.config(bg = bg)

	firstFrame.iconbitmap('docs/favicon.ico')

	v = IntVar()
	#<--Elements
	label = Label(firstFrame, text = 'CHOOSE PLOT:', bg=bg, fg=fg)
	firstFrameElements.append(label)

	radio1 = Radiobutton(firstFrame, text="Linear function", variable=v, value=1)
	radio2 = Radiobutton(firstFrame, text="Quadratic function", variable=v, value=2)
	radio3 = Radiobutton(firstFrame, text="Cubic function", variable=v, value=3)
	radio4 = Radiobutton(firstFrame, text="Hyperbola function", variable=v, value=4)
	radio5 = Radiobutton(firstFrame, text="Square function", variable=v, value=5)
	radio6 = Radiobutton(firstFrame, text="Sine function", variable=v, value=6)
	radio7 = Radiobutton(firstFrame, text="Cosine function", variable=v, value=7)
	radio8 = Radiobutton(firstFrame, text="Quadratic trinomial", variable=v, value=8)
	radio9 = Radiobutton(firstFrame, text="Factorial function", variable=v, value=9)
	radio10 = Radiobutton(firstFrame, text="|Linear| function", variable=v, value=10)

	firstFrameElements.append(radio1)
	firstFrameElements.append(radio2)
	firstFrameElements.append(radio3)
	firstFrameElements.append(radio4)
	firstFrameElements.append(radio5)
	firstFrameElements.append(radio6)
	firstFrameElements.append(radio7)
	firstFrameElements.append(radio8)
	firstFrameElements.append(radio9)
	firstFrameElements.append(radio10)

	button = Button(firstFrame, text = 'DRAW FUNCTION', command = lambda: input_arg(v, lang))
	NLlabel = Label(firstFrame, text = 'NameLess Corporation')

	firstFrameElements.append(button)
	#<--Configs
	label.config(font = ('Arial', 15, 'bold'))

	radio1.config(bg = bg, fg = fg, selectcolor = 'black')
	radio2.config(bg = bg, fg = fg, selectcolor = 'black')
	radio3.config(bg = bg, fg = fg, selectcolor = 'black')
	radio4.config(bg = bg, fg = fg, selectcolor = 'black')
	radio5.config(bg = bg, fg = fg, selectcolor = 'black')
	radio6.config(bg = bg, fg = fg, selectcolor = 'black')
	radio7.config(bg = bg, fg = fg, selectcolor = 'black')
	radio8.config(bg = bg, fg = fg, selectcolor = 'black')
	radio9.config(bg = bg, fg = fg, selectcolor = 'black')
	radio10.config(bg = bg, fg = fg, selectcolor = 'black')

	radio1.select()

	button.config(font = ('Arial', 12, 'bold'))
	NLlabel.config(font = ('Arial', 10, 'bold'), bg = bg, fg = fg)
	#<--Grids
	label.grid(column = 0, row = 0)

	radio1.grid(column = 0, row = 1, sticky = W, padx=30)
	radio2.grid(column = 0, row = 2, sticky = W, padx=30)
	radio3.grid(column = 0, row = 3, sticky = W, padx=30)
	radio4.grid(column = 0, row = 4, sticky = W, padx=30)
	radio5.grid(column = 0, row = 5, sticky = W, padx=30)
	radio6.grid(column = 0, row = 6, sticky = W, padx=30)
	radio7.grid(column = 0, row = 7, sticky = W, padx=30)
	radio8.grid(column = 0, row = 8, sticky = W, padx=30)
	radio9.grid(column = 0, row = 9, sticky = W, padx=30)
	radio10.grid(column = 0, row = 10, sticky = W, padx=30)

	button.grid(column = 0, row = 11)
	NLlabel.grid(column = 0, row = 12)

	main_menu = Menu(firstFrame)
	firstFrame.config(menu = main_menu)
	lang_menu = Menu(main_menu)
	info_menu = Menu(main_menu)

	main_menu.add_cascade(label="Language", menu = lang_menu)
	main_menu.add_cascade(label="Info", menu = info_menu)

	lang_menu.add_command(label="English", command = set_eng)
	lang_menu.add_command(label="Russian", command = set_rus)
	info_menu.add_command(label="Help", command = lambda: info(lang))
	info_menu.add_command(label="Authors", command = authors)
	#<--Start
	firstFrame.mainloop()


if __name__ == '__main__':
	mainFrame()