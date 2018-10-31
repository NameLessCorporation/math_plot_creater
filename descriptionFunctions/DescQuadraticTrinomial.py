
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import numpy as np
from math import *
from ezprint import *
from tkinter import *
import matplotlib.pyplot as plt
from functions.quadraticTrinomial import *


def main_frame(a, b, c, D, xo, yo, x_null_0, x_null_1, x_null_2, x_list, y_list):
	global thirdFrame

	#<--Settings for secondFrame
	thirdFrame = Tk()

	thirdFrame.title(str(a) + ' * ' + 'x' + '^2 * ' + str(b) + ' * ' + 'x * ' + str(c))

	thirdFrame.resizable(0, 0)

	thirdFrame.config(bg = '#1FA7E1')
	thirdFrame.config()

	#<--Elements
	label1 = Label(thirdFrame, text = 'Your args:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c), bg='#1FA7E1', fg='white')
	label2 = Label(thirdFrame, text = 'Discriminant: ' + str(D), bg='#1FA7E1', fg='white')
	label3 = Label(thirdFrame, text = 'TOPS FUNC.', bg='#1FA7E1', fg='white')
	label4 = Label(thirdFrame, text = 'x tops: ' + str(xo), bg='#1FA7E1', fg='white')
	label5 = Label(thirdFrame, text = 'y tops: ' + str(yo), bg='#1FA7E1', fg='white')
	label6 = Label(thirdFrame, text = 'NULL FUNC.', bg='#1FA7E1', fg='white')
	label7 = Label(thirdFrame, text = 'x_0 null: ' + str(x_null_0), bg='#1FA7E1', fg='white')
	label8 = Label(thirdFrame, text = 'x_1 null: ' + str(x_null_1), bg='#1FA7E1', fg='white')
	label9 = Label(thirdFrame, text = 'x_2 null: ' + str(x_null_2), bg='#1FA7E1', fg='white')
	label10 = Label(thirdFrame, text = 'PROPERTIES:', bg='#1FA7E1', fg='white')
	label11 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=[0; +∞)\n3) Even function\n4)The function decreases in the interval (-∞; 0)\n  The function increases in the interval (0; +∞)\n5) Asymptote has not', bg='#1FA7E1', fg='white')
	label12 = Label(thirdFrame, text = '6) Min value of x: ' + str(round(np.amin(x_list), 5)) + '\n   Min value of y: ' + str(round(min(y_list), 5)), bg='#1FA7E1', fg='white')
	label13 = Label(thirdFrame, text = '   Max value of x: ' + str(round(np.amax(x_list), 5)) + '\n   Max value of y: ' + str(round(max(y_list), 5)), bg='#1FA7E1', fg='white')

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
	label12.config(font = ('Arial', 15, 'bold'))
	label13.config(font = ('Arial', 15, 'bold'))

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
	label12.grid(column = 0, row = 11)
	label13.grid(column = 0, row = 12)

	#<--Start
	thirdFrame.mainloop()