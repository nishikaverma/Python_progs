from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog    # 'filedialog' is a submodule of 'tkinter' module"
from tkinter import messagebox    # 'messagebox' is a submodule of 'tkinter' module"

obj = Tk()
obj.geometry("400x400")
def accept():
    col=colorchooser.askcolor(color="green",title="choose any color for your window")
    if  col[0]!=None :
        obj['bg']=col[1]
    else:
        messagebox.showinfo("!",'please select any color...')
b = Button(obj, text="click me", command=accept)
b.pack()

obj.mainloop()
