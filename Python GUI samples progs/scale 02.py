from tkinter import *

obj=Tk()
obj.geometry("400x400")
def callR(x):
    x=hex(int(x))
    x_sliced=x[2:]
    if len(x_sliced)==1:
        num="#0"+str(x_sliced)+"0000"
    else:
        num = "#" + str(x_sliced) + "0000"
    obj.config(bg=num)

def callG(x):
    x=hex(int(x))
    x_sliced=x[2:]
    if len(x_sliced)==1:
        num="#000"+str(x_sliced)+"00"
    else:
        num = "#00" + str(x_sliced) + "00"
    obj.config(bg=num)
def callB(x):
    x=hex(int(x))
    x_sliced=x[2:]
    if len(x_sliced)==1:
        num="#00000"+str(x_sliced)
    else:
        num = "#0000" + str(x_sliced)
    obj.config(bg=num)

s1=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=callR)
s1.pack()
s2=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=callG)
s2.pack()
s3=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=callB)
s3.pack()
obj.config(bg='#000000')
obj.mainloop()
