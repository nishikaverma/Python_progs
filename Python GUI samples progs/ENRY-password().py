from tkinter import *
obj=Tk()
obj.geometry("400x400")
l=Label(obj,text="Enter password:")
e=Entry(obj,show="*")
l.grid(row=0,column=0)
e.grid(row=0,column=1)
obj.mainloop()