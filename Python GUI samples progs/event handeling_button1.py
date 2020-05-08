from tkinter import *

def fun():
    print("welcome to python")

obj=Tk()

b=Button(obj,text="click me",command=fun,)
b.pack()

obj.mainloop()