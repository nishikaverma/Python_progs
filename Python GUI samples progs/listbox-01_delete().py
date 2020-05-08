from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry("400x400")
l=Listbox(obj,bg='yellow')
sports=["cricket","football","hockey","baseball","vollyball","tennis","rugby","snooker","badminton"]

for i in sports:
    l.insert(END,i)
print(l.get(0))
print(l.get(0,END))
print(l.get(0,100)) # ignores out of indices
print(l.get(0,-4)) # ignores -ve indexing
print(l.size())
l.grid(row=0,column=0)
l.delete(0,4)
print(l.size())
obj.mainloop()