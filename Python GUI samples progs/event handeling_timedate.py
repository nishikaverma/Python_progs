from tkinter import  *
import datetime

def time():
    #l.config(text=datetime.datetime.now())
    date=datetime.datetime.now()
    l.config(text=date.strftime("%d-%B-%Y"))
obj=Tk()
b1=Button(obj, text="click here",command=time)

l=Label(obj,text="click the button for current date and time")

b1.pack()
l.pack()

obj.mainloop()