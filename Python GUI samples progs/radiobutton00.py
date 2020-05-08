from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry("400x400")

def show():
    if x.get()==1:
        messagebox.showinfo("INFO","your gender is Male")
    else:
        messagebox.showinfo("INFO", "your gender is Female")

x=IntVar()
l=Label(obj,text="select your gender")
r1=Radiobutton(obj,text="male",variable=x,value=1,command=show)
r2=Radiobutton(obj,text="female",variable=x,value=0,command=show)
l.pack()
r1.pack()
r2.pack()
obj.mainloop()