from tkinter import *
obj=Tk()

def Showit():
    e3.delete(0,END)
    e3.insert(0,e1.get()+' '+e2.get())
def Quit():
    sys.exit(0)
    #obj.distroy()

obj.geometry("400x400")

lab1=Label(obj, text=" First name")
lab2=Label(obj, text="Last name")
lab3=Label(obj,text="you typed")


e1=Entry(obj)
e2=Entry(obj)
e3=Entry(obj)


b1=Button(obj, text="show",command=Showit)
b2=Button(obj, text="quit",command=Quit)

lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=2,column=0,)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1,sticky=W)
obj.mainloop()
