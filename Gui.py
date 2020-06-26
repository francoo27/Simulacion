import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib 
from matplotlib import style
import tkinter as tk
from tkinter import ttk

import numpy as np
style.use("ggplot")
LARGE_FONT = ("Verdana",12)
# style.use("ggplot")


class SeaOfBTCapp(tk.Tk):
        def __init__(self,*args,**kwargs):
            tk.Tk.__init__(self,*args,**kwargs)
            # tk.Tk.iconbitmap(self,default="clienticon.ico")
            tk.Tk.wm_title(self,"MM1")
            container = tk.Frame(self)
            container.pack(side = "top",fill="both",expand=True)
            container.grid_rowconfigure(0,weight=1)
            container.grid_columnconfigure(0,weight=1)
            self.frames ={}
            
            frame = StartPage(container,self)
            frame.winfo_width = 1000
            self.frames[StartPage] = frame
            frame.grid(row=0,column=0,sticky="nsew")
            self.show_frame(StartPage)
        
        def show_frame(self,cont):
            frame = self.frames[cont]
            frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text ="Simulacion MM1",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button = ttk.Button(self,text="visit page 1",
                                command =lambda: print("AAAAAAA")  )
        button.pack()
        # entryExample = tk.Entry(self)
        # entryExample.place(x = 10,
        #                 y = 10,
        #                 width=200,
        #                 height=100)
        f = Figure(figsize=(5,5),dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)


app=SeaOfBTCapp()
app.geometry("800x600")
app.mainloop()