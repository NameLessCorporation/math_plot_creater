
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
from ezprint import *
from tkinter import *


def info():
		#<--Settings for secondFrame
	fourthFrame = Tk()

	fourthFrame.title('Info')

	fourthFrame.resizable(0, 0)

	fourthFrame.config(bg = '#1FA7E1')
	fourthFrame.config()

	#<--Elements
	label2 = Label(fourthFrame, text = 'Linear function - y=k(x-a)+b', bg='#1FA7E1', fg='white')
	label3 = Label(fourthFrame, text = 'Quadratic function - y=k(x-a)^2+b', bg='#1FA7E1', fg='white')
	label4 = Label(fourthFrame, text = 'Square function - k*sqrt(x-a)+b', bg='#1FA7E1', fg='white')
	label5 = Label(fourthFrame, text = 'Cubic function - y=k(x-a)^3+b', bg='#1FA7E1', fg='white')
	label6 = Label(fourthFrame, text = 'Hyperbola function - k/(x-a)+b', bg='#1FA7E1', fg='white')
	label7 = Label(fourthFrame, text = 'Sine function - y=k*sin(x-a)+b', bg='#1FA7E1', fg='white')
	label8 = Label(fourthFrame, text = 'Cosine function - y=k*cos(x-a)+b', bg='#1FA7E1', fg='white')
	label9 = Label(fourthFrame, text = 'QuadraticTrinomial - y=ax^2+bx+c', bg='#1FA7E1', fg='white')

	#<--Configs
	label2.config(font = ('Arial', 15, 'bold'))
	label3.config(font = ('Arial', 15, 'bold'))
	label4.config(font = ('Arial', 15, 'bold'))
	label5.config(font = ('Arial', 15, 'bold'))
	label6.config(font = ('Arial', 15, 'bold'))
	label7.config(font = ('Arial', 15, 'bold'))
	label8.config(font = ('Arial', 15, 'bold'))
	label9.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label2.grid(column = 0, row = 0)
	label3.grid(column = 0, row = 1)
	label4.grid(column = 0, row = 2)
	label5.grid(column = 0, row = 3)
	label6.grid(column = 0, row = 4)
	label7.grid(column = 0, row = 5)
	label8.grid(column = 0, row = 6)
	label9.grid(column = 0, row = 7)

	#<--Start
	fourthFrame.mainloop()


def authors():
	#<--Settings for secondFrame
	fourthFrame = Tk()

	fourthFrame.title('Info')

	fourthFrame.resizable(0, 0)

	fourthFrame.config(bg = '#1FA7E1')
	fourthFrame.config()

	#<--Elements
	label1 = Label(fourthFrame, text = 'Authors:', bg='#1FA7E1', fg='white')
	label2 = Label(fourthFrame, text = 'Midaef: midaef.ru', bg='#1FA7E1', fg='white')
	label3 = Label(fourthFrame, text = 'Stdian: stdian.ru', bg='#1FA7E1', fg='white')
	label4 = Label(fourthFrame, text = 'We would be grateful if you would donate us a Cup of coffee)', bg='#1FA7E1', fg='white')
	label5 = Label(fourthFrame, text = 'Webmoney midaef: WMR R381836540599, WMZ Z286377765031', bg='#1FA7E1', fg='white')
	label6 = Label(fourthFrame, text = 'Webmoney stdian: WMR R477293942800, WMZ Z187982353639', bg='#1FA7E1', fg='white')

	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))
	label2.config(font = ('Arial', 15, 'bold'))
	label3.config(font = ('Arial', 15, 'bold'))
	label4.config(font = ('Arial', 15, 'bold'))
	label5.config(font = ('Arial', 15, 'bold'))
	label6.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)
	label3.grid(column = 0, row = 2)
	label4.grid(column = 0, row = 3)
	label5.grid(column = 0, row = 4)
	label6.grid(column = 0, row = 5)

	#<--Start
	fourthFrame.mainloop()