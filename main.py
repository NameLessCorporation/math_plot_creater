
#<--Import lib
import matplotlib.pyplot as plt
from ezprint import *
from tkinter import *
import numpy as np
import decimal
#<--Import functions wish file-->
from functions.cubic import *
from functions.linear import *
from functions.square import *
from functions.quadratic import *
from functions.hyperbola import *

root = None
root1 = None
v = None

k = None
a = None
b = None


def draw():
	global k
	global a
	global b

	if v.get() == 1:
		creat_linear(int(k), int(a), int(b))
	elif v.get() == 2:
		creat_quadratic(int(k), int(a), int(b))
	elif v.get() == 3:
		creat_cubic(int(k), int(a), int(b))
	elif v.get() == 4:
		creat_hyperbola(int(k), int(a), int(b))
	elif v.get() == 5:
		creat_square(int(k), int(a), int(b))

def creat_plot():
	global root1
	global v
	global k
	global a
	global b

	k = k.get()
	a = a.get()
	b = b.get()
	root1.destroy()
	draw()
	


def input_arg():
	global root
	global root1
	global k
	global a
	global b
	#<--Settings for root
	root.destroy()
	root1 = Tk()

	root1.title('PLOT_CREATER')

	root1.resizable(0, 0)

	root1.config(bg = '#1FA7E1')
	root1.config()

	#<--Elements
	label1 = Label(root1, text = 'Input k:', bg='#1FA7E1', fg='white')

	k = Entry(root1, width = 20)

	label2 = Label(root1, text = 'Input a:', bg='#1FA7E1', fg='white')

	a = Entry(root1, width = 20)

	label3 = Label(root1, text = 'Input b:', bg='#1FA7E1', fg='white')

	b = Entry(root1, width = 20)

	button = Button(root1, text = 'Watch weather', command = creat_plot)

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
	root1.mainloop()


def main():
	global root
	global v
	#<--Settings for root
	root = Tk()

	root.title('PLOT_CREATER')

	root.resizable(0, 0)

	root.config(bg = '#1FA7E1')
	root.config()

	v = IntVar()
	#<--Elements
	label = Label(root, text = 'CHOOSE PLOT:', bg='#1FA7E1', fg='white')

	radio1 = Radiobutton(root, text="Linear function", variable=v, value=1)
	radio2 = Radiobutton(root, text="Quadratic function", variable=v, value=2)
	radio3 = Radiobutton(root, text="Cubic function", variable=v, value=3)
	radio4 = Radiobutton(root, text="Hyperbola function", variable=v, value=4)
	radio5 = Radiobutton(root, text="Square function", variable=v, value=5)

	button = Button(root, text = 'CREAT PLOT', command = input_arg)
	#<--Configs
	label.config(font = ('Arial', 15, 'bold'))

	radio1.config(bg = '#1FA7E1')
	radio2.config(bg = '#1FA7E1')
	radio3.config(bg = '#1FA7E1')
	radio4.config(bg = '#1FA7E1')
	radio5.config(bg = '#1FA7E1')

	radio1.select()

	button.config(font = ('Arial', 15, 'bold'))
	#<--Grids
	label.grid(column = 0, row = 0)

	radio1.grid(column = 0, row = 1)
	radio2.grid(column = 0, row = 2)
	radio3.grid(column = 0, row = 3)
	radio4.grid(column = 0, row = 4)
	radio5.grid(column = 0, row = 5)

	button.grid(column = 0, columnspan = 2)
	#<--Start
	root.mainloop()


if __name__ == '__main__':
	main()