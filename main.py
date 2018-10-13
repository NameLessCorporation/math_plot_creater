
#<--Import lib
import sys
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt
#<--Import functions wish file-->
from functions.cubic import *
from functions.linear import *
from functions.quadratic import *

v = None


def creat_plot():
	global v
	if v.get() == 1:
		creat_linear()
	elif  v.get() == 2:
		creat_quadratic()
	elif v.get() == 3:
		creat_cubic()


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

	button = Button(root, text = 'CREAT PLOT', command = creat_plot)
	#<--Configs
	label.config(font = ('Arial', 15, 'bold'))

	radio1.config(bg = '#1FA7E1')
	radio2.config(bg = '#1FA7E1')
	radio3.config(bg = '#1FA7E1')

	button.config(font = ('Arial', 15, 'bold'))
	#<--Grids
	label.grid(column = 0, row = 0)

	radio1.grid(column = 0, row = 1)
	radio2.grid(column = 0, row = 2)
	radio3.grid(column = 0, row = 3)

	button.grid(column = 0, columnspan = 2)
	#<--Start
	root.mainloop()


if __name__ == '__main__':
	main()