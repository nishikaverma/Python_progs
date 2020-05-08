from tkinter import *
obj=Tk()
obj.geometry("400x400")
def colorit():
    obj.config(bg=x.get())

old_col=obj["bg"]
x=StringVar()
c=Checkbutton(obj,variable=x,text="Red",command=colorit,onvalue="red",offvalue=old_col)
c.deselect() # deselects the checkbutton ,by default
c.pack()

obj.mainloop()