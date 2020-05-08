from tkinter import *
def fun(e):
    key = e.char
    if key=="r":
        obj['bg']="red"
    if key=="b":
        obj['bg']="blue"
    if key=="g":
        obj['bg']="green"

obj=Tk()
obj.geometry("400x400")
obj.bind("<Key>",fun)
#obj.bind("r",lambda e:obj.config(bg="red"))
#obj.bind("b",lambda e:obj.config(bg="blue"))
#obj.bind("g",lambda e:obj.config(bg="green"))

obj.mainloop()