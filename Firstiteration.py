"""
Created on Mon Feb 27 19:02:32 2017

@author: Simon
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter import Label
from tkinter import *
from tkinter import messagebox
from math import log10, floor
import numpy as np
from numba import jit

from matplotlib import pyplot as plt
from matplotlib import colors
def round_sig(x, sig=7):
        return round(x, sig-int(floor(log10(abs(x))))-1)


#maths and display code derived/inspired from Jean Francois Puget 
#https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift?lang=en
@jit
def julia(z,maxiter,horizon,log_horizon): #a new function, where the basic mandelbrot factal formula will be declared
    f = complex(-0.75, 0.15)
    #complex(-0.1, 0.65) #setting a C to Z C in the formula is a complex numbers
    for n in range(maxiter): #this for loop is getting the number of iterations (clearity)
        az = abs(z) #abosolute, this is also setting up for the next part is integral to plotting this fravtal
        if az > horizon: #the horizon is 2, the magic number  for the mandelbrot set, if the number produced is less than 2 it is black
            return n - np.log(np.log(az))/np.log(2) + log_horizon #here those valus are reuturn to this formula will help in the shading between colors on the the next funct
        z = z*z + f #this is the formula
    return 0


@jit  #this decorator implements the numPy library
def mandelbrot(z,maxiter,horizon,log_horizon): #a new function, where the basic mandelbrot factal formula will be declared

    s = z
        
    #complex(-0.1, 0.65) #setting a C to Z C in the formula is a complex numbers
    for n in range(maxiter): #this for loop is getting the number of iterations (clearity)
        az = abs(z) #abosolute, this is also setting up for the next part is integral to plotting this fravtal
        if az > horizon: #the horizon is 2, the magic number  for the mandelbrot set, if the number produced is less than 2 it is black
            return n - np.log(np.log(az))/np.log(2) + log_horizon #here those valus are reuturn to this formula will help in the shading between 
                                                                  #colors on the the next function
        z = z*z + s #this is the formula
    return 0#these two lines show that if the number is instantly infinity a zero is returned, meaning it is out of out domain 

@jit #this decorator implements the numPy library
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):#a new function, here the basic mandelbrot dimesinos will be created
    horizon = 2.0 ** 40 #this is creating the size of the image that will be displayed
    log_horizon = np.log(np.log(horizon))/np.log(2) # this is the same string of numbers from before, her the horizon is being deed for display
    rx = np.linspace(xmin, xmax, width) #this line is list that is creating the x axis
    ry = np.linspace(ymin, ymax, height)# this line is list that is creating the y axis
    n1 = np.empty((width,height))# this line is creating the base for where the image will be plotted in
    for i in range(width): #this for loop is identifying each point in the x axis as well as the ticks for the plot
        for j in range(height): #this for loop is identifying each point in the y axis as well as the ticks for the plot
            n1[i,j] = mandelbrot(rx[i] + 1j*ry[j],maxiter,horizon, log_horizon) #this is creating the entire plot but only within the computer
                                                                                #this plot still needs to be drawn foward
    return (rx,ry,n1) #returns the values created for sue in the display


def mandelbrot_image(ax, xmin=-2.0,xmax=0.5,ymin=-1.25,ymax=1.25,width=10,height=10,
             maxiter=2048,cmap='hot',gamma=0.3): #the coords and cmap are essentially a filler for the imput in the plot() function at the bottom of the code


    dpi = 80
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)

    ticks = np.arange(0,img_width,3*dpi)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    ax.set_xticks(ticks); ax.set_xticklabels(x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    ax.set_yticks(ticks); ax.set_yticklabels(y_ticks)
    ax.set_title("The Mandelbrot set")
    norm = colors.PowerNorm(gamma)
    ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm)



global gammaz
gammaz = 0.3

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMOL_FONT= ("Verdana", 8)
SMOLL_FONT= ("Verdana", 6)


    
    

def AboutWindow(msg):
    popup = tk.Tk()
    popup.wm_title("about")
    label = ttk.Label(popup, text=msg, font=SMOL_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    

def helpz():
    popup = tk.Tk()
    popup.wm_title("Coordinates & Help")
    labe = ttk.Label(popup, text="(xmin,xmax,ymin,ymax)", font=NORM_FONT)
    labe.pack(side="top", fill="x", pady=10)
    label = ttk.Label(popup, text="Base coordinates: -2.0,0.5,-1.25,1.25", font=SMOL_FONT)
    label.pack(side="top", fill="x", pady=10)
    label1 = ttk.Label(popup, text="Seahorse valley coordinates: -0.8,-0.7,0,0.1", font=SMOL_FONT)
    label1.pack(side="top", fill="x", pady=10)
    label2 = ttk.Label(popup, text="Small mandelbrot coordinates: -1.82,-1.72,-0.06,0.06", font=SMOL_FONT)
    label2.pack(side="top", fill="x", pady=10)
    label3 = ttk.Label(popup, text="Scepter Variant coordinates: -1.110,-1.105,0.226,0.231", font=SMOL_FONT)
    label3.pack(side="top", fill="x", pady=10)
    label4 = ttk.Label(popup, text="Quad-Spiral Valley coordinates: 0.273,0.279,0.482,0.487", font=SMOL_FONT)
    label4.pack(side="top", fill="x", pady=10)
    label5 = ttk.Label(popup, text="gay pride coordinates: 0.273,0.275,0.481,0.483", font=SMOL_FONT)
    label5.pack(side="top", fill="x", pady=10)
    label6 = ttk.Label(popup, text="Replications and a x coordinates: -0.745437,-0.745419 ,0.113000, 0.113018", font=SMOL_FONT)
    label6.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def Settings():
    popup = tk.Tk()
    #tk.Tk.iconbitmap(default ="set.ico")
    popup.wm_title("Coordinates")
    msg = "Enter the coordinates for the section of the Mandelbrot set you would like to render"
    fil = ttk.Label(popup, text = msg, font=SMOL_FONT)
    fil.pack(side="top", fill="x", pady=10)
    cooinfo = ttk.Button(popup, text = "help", command=lambda: helpz())
    cooinfo.pack()
    
    
    label1 = ttk.Label(popup, text="xmin", font=SMOL_FONT)
    label1.pack(side="top", fill="x", pady=10)
    e1 = tk.Entry(popup)
    e1.pack(side="top", fill="x")
    xminvar = e1.get()
    
    label2 = ttk.Label(popup, text="xmax", font=SMOL_FONT)
    label2.pack(side="top", fill="x", pady=10)
    e2 = tk.Entry(popup)
    e2.pack(side="top", fill="x")
    xmaxvar = e1.get()
    
    label3 = ttk.Label(popup, text="ymin", font=SMOL_FONT)
    label3.pack(side="top", fill="x", pady=10)
    e3 = tk.Entry(popup)
    e3.pack(side="top", fill="x")
    yminvar = e1.get()
    
    label4 = ttk.Label(popup, text="ymax", font=SMOL_FONT)
    label4.pack(side="top", fill="x", pady=10)
    e4 = tk.Entry(popup)
    e4.pack(side="top", fill="x")
    ymaxvar = e1.get()
    label4.bind("<Up>", arrow)
       
    B1 = ttk.Button(popup, text="Apply", command = popup.destroy)
    B1.pack()

    def arrow(event):
        print("poop")

class base(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, "iconz.ico")
        tk.Tk.wm_title(self, "Fractal Renderer (by Simon Mahns)")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_separator()
        #filemenu.add_command(label="Settings", command=lambda: Settings())
        filemenu.add_command(label="Julia Set", command = lambda: AboutWindow("go to main menu"))
        filemenu.add_command(label="About", command = lambda: AboutWindow("THIS WAS A FUN PROJECT"))
        filemenu.add_separator()
        menubar.add_cascade(label="File", menu=filemenu)
        
        preferences = tk.Menu(menubar, tearoff=1)
        preferences.add_command(label="Help", command=lambda: helpz())
        filemenu.add_separator()
        menubar.add_cascade(label="Coordinates", menu=preferences)
        tk.Tk.config(self, menu=menubar)
        
        self.frames = {}

        for F in (JuliaPage,  MainPage, StartPage):

            frame = F(container, self)
            
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="The Mandelbrot set", command=lambda: controller.show_frame(MainPage))
        
        buttona = ttk.Button(self, text ="The Julia Set", command=lambda: controller.show_frame(JuliaPage) )
        button.pack()
        buttona.pack()
        

        

class JuliaPage(tk.Frame):   
        
    
    
    @jit
    def julia_set(xmin,xmax,ymin,ymax,width,height,maxiter):#a new function, here the basic mandelbrot dimesinos will be created
        horizon = 2.0 ** 40 #this is creating the size of the image that will be displayed
        log_horizon = np.log(np.log(horizon))/np.log(2) # this is the same string of numbers from before, her the horizon is being determined for display
        rx = np.linspace(xmin, xmax, width) #this line is list that is creating the x axis
        ry = np.linspace(ymin, ymax, height)# this line is list that is creating the y axis
        n1 = np.empty((width,height))# this line is creating the base for where the image will be plotted in
        for i in range(width): #this for loop is identifying each point in the x axis as well as the ticks for the plot
            for j in range(height): #this for loop is identifying each point in the y axis as well as the ticks for the plot
                n1[i,j] = julia(rx[i] + 1j*ry[j],maxiter,horizon, log_horizon) #this is creating the entire plot but only within the computer
                                                                                #this plot still needs to be drawn foward
        return (rx,ry,n1)

    def julia_image(ax, xmin=-2.0,xmax=0.5,ymin=-1.25,ymax=1.25,width=10,height=10,\
             maxiter=2048,cmap='hot',gamma=0.3): #the coords and cmap are essentially a filler for the imput in the plot() function at the bottom of the code
        print (xmin, xmax,ymax, ymin, width, height, maxiter)
        dpi = 80
        img_width = dpi * width
        img_height = dpi * height
        x,y,z = JuliaPage.julia_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)

        ticks = np.arange(0,img_width,3*dpi)
        x_ticks = xmin + (xmax-xmin)*ticks/img_width
        ax.set_xticks(ticks); ax.set_xticklabels(x_ticks)
        y_ticks = ymin + (ymax-ymin)*ticks/img_width
        ax.set_yticks(ticks); ax.set_yticklabels(y_ticks)
        ax.set_title("The Julia set")
        norm = colors.PowerNorm(gamma)
        ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm)

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'white')
       # root = tk.Tk()
        controller.bind('<Left>', lambda event: JuliaPage.left(self))
        controller.bind('<Right>', lambda event: JuliaPage.right(self))
        controller.bind('<Up>', lambda event: JuliaPage.up(self))
        controller.bind('<Down>', lambda event: JuliaPage.down(self))
        controller.bind('<Return>', lambda event: JuliaPage.home(self))
        controller.bind('<x>', lambda event: JuliaPage.zoomin(self))
        
        values = ['jet', 'rainbow', 'ocean', 'hot', 'cubehelix','gnuplot','terrain','prism', 'pink']  
        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM)
        
        button2 = ttk.Button(self, text="Re-Render",command=self.plot_julia)
        button2.pack(side = TOP)

        self.combobox = ttk.Combobox(self, values=values)
        self.combobox.current(0)
        self.combobox.pack(side = BOTTOM)

        
        label2 = ttk.Label(self, text="choose your flavor", font=SMOL_FONT)
        label2.pack (side = BOTTOM)
               
            
        label11 = ttk.Label(self, text="xmin", font=SMOLL_FONT)
        label11.pack()
        self.e1 = tk.Entry(self)
        self.e1.insert(0, -2.0)
        self.e1.pack()
        
    
        label22 = ttk.Label(self, text="xmax", font=SMOLL_FONT)
        label22.pack()
        self.e2 = tk.Entry(self)
        self.e2.insert(0, 2.0 )
        self.e2.pack()
        
    
        label33 = ttk.Label(self, text="ymin", font=SMOLL_FONT)
        label33.pack()
        self.e3 = tk.Entry(self)
        self.e3.insert(0, -2.0)
        self.e3.pack()
        
    
        label44 = ttk.Label(self, text="ymax", font=SMOLL_FONT)
        label44.pack()
        self.e4 = tk.Entry(self)
        self.e4.insert(0, 2.0)
        self.e4.pack()
        
        self.width, self.height = 10, 10
        fig = Figure(figsize=(self.width, self.height))
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.show()
        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand=True)
        
        self.plot_julia()
    
        
    def left(self):
        print("You hit left.")  
        xxmin = float(self.e1.get())
        xxmax = float(self.e2.get())
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        xxmin = (xxmin - ((abs(xxmin - xxmax))/3))
        xxmax = (xxmax - ((abs(xxmin - xxmax))/3))
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        print (xxmax)
        print (xxmin)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e1.insert(0, xxmin)
        self.e2.insert(0, xxmax)
        self.plot_julia()
    
    def right(self):
        print("You hit right.")  
        xxmin = float(self.e1.get())
        xxmax = float(self.e2.get())
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        xxmin = (xxmin + ((abs(xxmin - xxmax))/3))
        xxmax = (xxmax + ((abs(xxmin - xxmax))/3))
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e1.insert(0, xxmin)
        self.e2.insert(0, xxmax)
        self.plot_julia()
    
    def up(self):
        print("You hit up.")  
        yymin = float(self.e3.get())
        yymax = float(self.e4.get())
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        yymin = (yymin + ((abs(yymin - yymax))/3))
        yymax = (yymax + ((abs(yymin - yymax))/3))
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e3.insert(0, yymin)
        self.e4.insert(0, yymax)
        self.plot_julia()
    
    def down(self):
        print("You hit down.")  
        yymin = float(self.e3.get())
        yymax = float(self.e4.get())
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        yymin = (yymin - ((abs(yymin - yymax))/3))
        yymax = (yymax - ((abs(yymin - yymax))/3))
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e3.insert(0, yymin)
        self.e4.insert(0, yymax)
        self.plot_julia()
        
    def zoomin(self):
        print("You hit down.")  
        xxmin = float(self.e1.get())
        xxmax = float(self.e2.get())
        yymin = float(self.e3.get())
        yymax = float(self.e4.get())
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        xxmin = (xxmin + ((abs(xxmin - xxmax))/3))
        xxmax = (xxmax - ((abs(xxmin - xxmax))/3))
        yymin = (yymin + ((abs(yymin - yymax))/3))
        yymax = (yymax - ((abs(yymin - yymax))/3))
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e1.insert(0, xxmin)
        self.e2.insert(0, xxmax)
        self.e3.insert(0, yymin)
        self.e4.insert(0, yymax)
        self.plot_julia()
    
    def home(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e1.insert(0, -2)
        self.e2.insert(0, 2)
        self.e3.insert(0, -2)
        self.e4.insert(0, 2)
        self.plot_julia()
        
        
        

        #while (god):
#             if keys[pygame.K_LEFT]:
#                 xxmin = int(self.e1.get())
#                 print (xxmin)
# ===========================================================================
            
    def plot_julia (self):
        colr = self.combobox.get()
        print (colr)
        self.ax.clear()
        xminvar = float (self.e1.get())
        xmaxvar = float (self.e2.get())
        yminvar = float (self.e3.get())
        ymaxvar = float (self.e4.get())
        print(xminvar)
        JuliaPage.julia_image(self.ax, xminvar, xmaxvar, yminvar, ymaxvar, cmap=colr, gamma=0.3)
        #mandelbrot_image(self.ax, -1.25,1.25 ,-1.25, 1.25,cmap=colr, gamma=0.4) #-0.745428   0.113009

        self.canvas.draw()
        
        
    
        

        



 
      
class MainPage(tk.Frame):
    
    

    global gammaz
    gammaz = 0.3
    def var_states(self):  
        print (self.combobox.get())
        print (self.colr)
        self.plot ()


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'white')
        
        values = ['jet', 'rainbow', 'ocean', 'hot', 'cubehelix','gnuplot','terrain','prism', 'pink']  
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM)
        button2 = tk.Button(self, text="Re-Render",command=self.plot)
        button2.pack(side = TOP)

        self.combobox = ttk.Combobox(self, values=values)
        self.combobox.current(0)
        self.combobox.pack(side = BOTTOM)

        
        label2 = ttk.Label(self, text="choose your flavor", font=SMOL_FONT)
        label2.pack (side = BOTTOM)
               
            
        label11 = ttk.Label(self, text="xmin", font=SMOLL_FONT)
        label11.pack()
        self.e1 = tk.Entry(self)
        self.e1.insert(0, -2.0)
        self.e1.pack()
        
    
        label22 = ttk.Label(self, text="xmax", font=SMOLL_FONT)
        label22.pack()
        self.e2 = tk.Entry(self)
        self.e2.insert(0, 0.5)
        self.e2.pack()
        
    
        label33 = ttk.Label(self, text="ymin", font=SMOLL_FONT)
        label33.pack()
        self.e3 = tk.Entry(self)
        self.e3.insert(0, -1.25)
        self.e3.pack()
        
    
        label44 = ttk.Label(self, text="ymax", font=SMOLL_FONT)
        label44.pack()
        self.e4 = tk.Entry(self)
        self.e4.insert(0, 1.25)
        self.e4.pack()
        
        self.width, self.height = 10, 10
        fig = Figure(figsize=(self.width, self.height))
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.show()
        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand=True)
        controller.bind('<a>', lambda event: MainPage.left(self))
        controller.bind('<d>', lambda event: MainPage.right(self))
        controller.bind('<w>', lambda event: MainPage.up(self))
        controller.bind('<s>', lambda event: MainPage.down(self))
        controller.bind('<r>', lambda event: MainPage.home(self))
        controller.bind('<q>', lambda event: MainPage.zoomin(self))
        self.plot ()

        
    def plot (self):
        colr = self.combobox.get()
        print (colr)
        self.ax.clear()
        xminvar = float (self.e1.get())
        xmaxvar = float (self.e2.get())
        yminvar = float (self.e3.get())
        ymaxvar = float (self.e4.get())
        print(xminvar)
        mandelbrot_image(self.ax, xminvar, xmaxvar, yminvar, ymaxvar, cmap=colr, gamma=0.3)
        #mandelbrot_image(self.ax, -1.25,1.25 ,-1.25, 1.25,cmap=colr, gamma=0.4) #-0.745428   0.113009

        self.canvas.draw()

    def left(self):
        print("You hit left.")  
        xxmin = float(self.e1.get())
        xxmax = float(self.e2.get())
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        xxmin = (xxmin - ((abs(xxmin - xxmax))/3))
        xxmax = (xxmax - ((abs(xxmin - xxmax))/3))
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        print (xxmax)
        print (xxmin)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e1.insert(0, xxmin)
        self.e2.insert(0, xxmax)
        self.plot()
    
    def right(self):
        print("You hit right.")  
        xxmin = float(self.e1.get())
        xxmax = float(self.e2.get())
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        xxmin = (xxmin + ((abs(xxmin - xxmax))/3))
        xxmax = (xxmax + ((abs(xxmin - xxmax))/3))
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e1.insert(0, xxmin)
        self.e2.insert(0, xxmax)
        self.plot()
    
    def up(self):
        print("You hit up.")  
        yymin = float(self.e3.get())
        yymax = float(self.e4.get())
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        yymin = (yymin + ((abs(yymin - yymax))/3))
        yymax = (yymax + ((abs(yymin - yymax))/3))
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e3.insert(0, yymin)
        self.e4.insert(0, yymax)
        self.plot()
    
    def down(self):
        print("You hit down.")  
        yymin = float(self.e3.get())
        yymax = float(self.e4.get())
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        yymin = (yymin - ((abs(yymin - yymax))/3))
        yymax = (yymax - ((abs(yymin - yymax))/3))
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e3.insert(0, yymin)
        self.e4.insert(0, yymax)
        self.plot()
        
    def zoomin(self):
        print("You hit down.")  
        xxmin = float(self.e1.get())
        xxmax = float(self.e2.get())
        yymin = float(self.e3.get())
        yymax = float(self.e4.get())
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        xxmin = (xxmin + ((abs(xxmin - xxmax))/3))
        xxmax = (xxmax - ((abs(xxmin - xxmax))/3))
        yymin = (yymin + ((abs(yymin - yymax))/3))
        yymax = (yymax - ((abs(yymin - yymax))/3))
        yymax= round_sig(yymax)
        yymin= round_sig(yymin)
        xxmax= round_sig(xxmax)
        xxmin= round_sig(xxmin)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e1.insert(0, xxmin)
        self.e2.insert(0, xxmax)
        self.e3.insert(0, yymin)
        self.e4.insert(0, yymax)
        self.plot()
    
    def home(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e1.insert(0, -2.0)
        self.e2.insert(0, 0.5)
        self.e3.insert(0, -1.25)
        self.e4.insert(0, 1.25)
        self.plot()

app = base()

app.geometry ("800x630")
app.mainloop()
