from tkinter import *

obj=Tk()
obj.geometry("400x400")
def call(x):
    x=hex(int(x))
    x_sliced=x[2:]
    if len(x_sliced)==1:
        num="#0"+str(x_sliced)+"0000"
    else:
        num = "#" + str(x_sliced) + "0000"
    obj.config(bg=num)

s=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s.pack()
obj.config(bg='#000000')
obj.mainloop()
