from tkinter import *
obj=Tk()

def Showit():
    l.config(text=e1.get()+" "+e2.get())

def Quit():
    exit(0)
    #obj.distroy()
obj.geometry("400x400")

lab1=Label(obj, text=" First name")
lab2=Label(obj, text="Last name")

e1=Entry(obj)
e2=Entry(obj)

l=Label(obj,font="Arial 10 bold")

b1=Button(obj, text="show",command=Showit)
b2=Button(obj, text="quit",command=Quit)

lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
l.grid(row=2,column=0,columnspan=2,sticky=W)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1,sticky=W)
obj.mainloop()
