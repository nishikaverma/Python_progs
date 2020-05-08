from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog    # 'filedialog' is a submodule of 'tkinter' module"
from tkinter import messagebox    # 'messagebox' is a submodule of 'tkinter' module"

obj=Tk()
def setcolor(value_str):

    value=hex(int(value_str))
    value_slice = value[2:]
    if len(value_slice)==1:
        value_slice="0"+value_slice
    value_slice="#"+value_slice+"0000"
    print(value_slice)
    obj.config(bg=value_slice)


obj.geometry("400x400")
s=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=setcolor)
obj.config(bg="#000000")
s.pack()

obj.mainloop()
