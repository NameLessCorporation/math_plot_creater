#!/usr/bin/python
# -*- coding: utf-8 -*-

# <--Import lib

import matplotlib.pyplot as plt
from ezprint import *
from tkinter import *
import numpy as np
import decimal

# <--Import functions wish file-->

from functions.cubic import *
from functions.linear import *
from functions.square import *
from functions.quadratic import *
from functions.hyperbola import *
from functions.sin import *

mainFrame = None
secondFrame = None
plot = None

k = None
a = None
b = None


def draw():
    global k
    global a
    global b

    if plot.get() == 1:
        creat_linear(float(k), float(a), float(b))
    elif plot.get() == 2:
        creat_quadratic(float(k), float(a), float(b))
    elif plot.get() == 3:
        creat_cubic(float(k), float(a), float(b))
    elif plot.get() == 4:
        creat_hyperbola(float(k), float(a), float(b))
    elif plot.get() == 5:
        creat_square(float(k), float(a), float(b))
    elif plot.get() == 6:
        creat_sin(float(k), float(a), float(b))


def creat_plot():
    global secondFrame
    global plot
    global k
    global a
    global b

    k = k.get()
    a = a.get()
    b = b.get()
    secondFrame.destroy()
    draw()


def input_arg():
    global mainFrame
    global secondFrame
    global k
    global a
    global b

    # <--Settings for root

    mainFrame.destroy()
    secondFrame = Tk()

    secondFrame.title('PLOT_CREATER')

    secondFrame.resizable(0, 0)

    secondFrame.config(bg='#1FA7E1')
    secondFrame.config()

    # <--Elements

    label1 = Label(secondFrame, text='Input k:', bg='#1FA7E1',
                   fg='white')

    k = Entry(secondFrame, width=20)

    label2 = Label(secondFrame, text='Input a:', bg='#1FA7E1',
                   fg='white')

    a = Entry(secondFrame, width=20)

    label3 = Label(secondFrame, text='Input b:', bg='#1FA7E1',
                   fg='white')

    b = Entry(secondFrame, width=20)

    button = Button(secondFrame, text='Draw', command=creat_plot)

    k.delete(0, END)
    k.insert(0, '1')

    a.delete(0, END)
    a.insert(0, '0')

    b.delete(0, END)
    b.insert(0, '0')

    # <--Configs

    label1.config(font=('Arial', 15, 'bold'))

    k.config(font=('Arial', 15, 'bold'))

    label2.config(font=('Arial', 15, 'bold'))

    a.config(font=('Arial', 15, 'bold'))

    label3.config(font=('Arial', 15, 'bold'))

    b.config(font=('Arial', 15, 'bold'))

    button.config(font=('Arial', 15, 'bold'))

    # <--Grids

    label1.grid(column=0, row=1)

    k.grid(column=0, row=2)

    label2.grid(column=0, row=3)

    a.grid(column=0, row=4)

    label3.grid(column=0, row=5)

    b.grid(column=0, row=6)

    button.grid(column=0, columnspan=7)

    # <--Start

    secondFrame.mainloop()


def main():
    global mainFrame
    global plot

    # <--Settings for root

    mainFrame = Tk()

    mainFrame.title('PLOT_CREATER')

    mainFrame.resizable(0, 0)

    mainFrame.config(bg='#1FA7E1')
    mainFrame.config()

    plot = IntVar()

    # <--Elements

    label = Label(mainFrame, text='CHOOSE PLOT:', bg='#1FA7E1',
                  fg='white')

    radio1 = Radiobutton(mainFrame, text='Linear function', variable=v,
                         value=1)
    radio2 = Radiobutton(mainFrame, text='Quadratic function',
                         variable=v, value=2)
    radio3 = Radiobutton(mainFrame, text='Cubic function', variable=v,
                         value=3)
    radio4 = Radiobutton(mainFrame, text='Hyperbola function',
                         variable=v, value=4)
    radio5 = Radiobutton(mainFrame, text='Square function', variable=v,
                         value=5)
    radio6 = Radiobutton(mainFrame, text='Sin function', variable=v,
                         value=6)

    button = Button(mainFrame, text='CREAT PLOT', command=input_arg)

    # <--Configs

    label.config(font=('Arial', 15, 'bold'))

    bg = '#1FA7E1'

    radio1.config()
    radio2.config(bg=bg)
    radio3.config(bg=bg)
    radio4.config(bg=bg)
    radio5.config(bg=bg)
    radio6.config(bg=bg)

    radio1.select()

    button.config(font=['Arial', 15, 'bold'])

    # <--Grids

    label.grid(column=0, row=0)

    radio1.grid(column=0, row=1)
    radio2.grid(column=0, row=2)
    radio3.grid(column=0, row=3)
    radio4.grid(column=0, row=4)
    radio5.grid(column=0, row=5)
    radio6.grid(column=0, row=6)

    button.grid(column=0, columnspan=2)

    # <--Start

    mainFrame.mainloop()


if __name__ == '__main__':
    main()
