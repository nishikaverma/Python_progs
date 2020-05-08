from tkinter import *
obj=Tk()
obj.geometry("400x400")
def colorit():
    if x.get()==1:
        obj.config(bg="red")
    else:
        obj.config(bg=old_col)
old_col=obj["bg"]
x=BooleanVar() # or x=IntVar()
c=Checkbutton(obj,text="Red",variable=x,command=colorit)
c.pack()
obj.mainloop()