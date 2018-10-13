
#<--Import lib
import sys
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt
#<--Import functions wish file-->
from functions.cubic import *
from functions.linear import *
from functions.square import *
from functions.quadratic import *
from functions.hyperbola import *

v = None

k = -1
a = 4
b = 4


def creat_plot():
	global v
	if v.get() == 1:
		creat_linear(k, a, b)
	elif  v.get() == 2:
		creat_quadratic(k, a, b)
	elif v.get() == 3:
		creat_cubic(k, a, b)
	elif v.get() == 4:
		creat_hyperbola(k, a, b)
	elif v.get() == 5:
		creat_square(k, a, b)

def main():
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

	button = Button(root, text = 'CREAT PLOT', command = creat_plot)
	#<--Configs
	label.config(font = ('Arial', 15, 'bold'))

	radio1.config(bg = '#1FA7E1')
	radio2.config(bg = '#1FA7E1')
	radio3.config(bg = '#1FA7E1')
	radio4.config(bg = '#1FA7E1')
	radio5.config(bg = '#1FA7E1')

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