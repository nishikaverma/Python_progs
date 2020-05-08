from tkinter import *

obj=Tk()
obj.geometry("400x400")

s=Scale(obj,from_=0,to=30,orient=HORIZONTAL)
s.pack()
obj.mainloop()
