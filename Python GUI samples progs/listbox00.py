from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry("400x400")
l=Listbox(obj,bg='yellow')
sports=["cricket","football","hockey","baseball","volliball","tanis","rugby","snooker","badminton"]
#x=0
for i in sports:
    l.insert(END,i) # or can be written as: l.insert(x,i)
    #x+=1

l.grid(row=0,column=0)
obj.mainloop()