from tkinter import *
obj=Tk()

lab1=Label(obj, text="name")
lab2=Label(obj, text="password")

e1=Entry(obj)
e2=Entry(obj)

b1=Button(obj, text="show")
b2=Button(obj, text="quit")


lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=0,column=1)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
obj.mainloop()
