from tkinter import *

obj=Tk()
obj.geometry("200x200")
color=str(obj['bg'])
obj.bind("<Return>",lambda e :obj.config(bg="red"))
obj.bind("<Escape>",lambda e :obj.config(bg=color))
obj.mainloop()