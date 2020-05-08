from tkinter import *

def count():

    num.set(num.get()+1)


obj=Tk()
num= IntVar()
b=Button(obj,text="click me",command=count)
#l=Label(obj)
l=Label(obj,textvariable=num)
b.pack()
l.pack()

obj.mainloop()