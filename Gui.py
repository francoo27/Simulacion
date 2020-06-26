from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib import style
from matplotlib import animation
style.use("ggplot")
LARGE_FONT = ("Verdana",12)
from random import randint


root = tk.Tk()
figure = Figure(figsize=(5, 4), dpi=100)
a = figure.add_subplot(111)
ffile = open("sampleData", 'w+')
ffile.close()

xList = [0]
yList = [0]


def animate(i):
    # ffile = open("sampleData", 'r')
    # pullData = ffile.read()
    # dataList = pullData.split('\n')
    # xList = []
    # yList = []
    # for eachLine in dataList:
    #     if len(eachLine) > 1:
    #         x,y = eachLine.split(',')
    #         xList.append(int(x))
    #         yList.append(int(y))
    xList.append(int(xList[-1]+randint(0,10)))
    yList.append(int(yList[-1]+randint(0,10)))
    a.clear()
    a.plot(xList,yList)


canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

ani = animation.FuncAnimation(figure, animate,interval=50)
root.mainloop()
