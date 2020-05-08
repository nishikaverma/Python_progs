from tkinter import *

def fun():

    l.config(text="welcome to python")
obj=Tk()

l=Label(obj)
b=Button(obj,text="click me",command=fun,)

b.pack()
l.pack()
obj.mainloop()