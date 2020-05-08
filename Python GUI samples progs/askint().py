from tkinter import *
from tkinter import messagebox # 'messagebox' is a submodule of 'tkinter' module"
from tkinter import simpledialog # 'simpledialog' is a submodule of 'tkinter' module"
obj=Tk()
obj.geometry("400x400")
def accept():
    ask=simpledialog.askinteger("input","Please enter your age...",minvalue=18,maxvalue=122)
    if ask is not None: # NONE  is a value of datatype 'none type'
        messagebox.showinfo("congrats","you are elegible fpr voting !")
b=Button(obj,text="click me",command=accept)
b.pack()

obj.mainloop()