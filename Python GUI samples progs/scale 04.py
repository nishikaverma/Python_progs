from tkinter import *

obj=Tk()
obj.geometry("400x400")
def call(x):
    xr=s1.get()
    xg=s2.get()
    xb=s3.get()

    xr=hex(int(xr))
    xg= hex(int(xg))
    xb= hex(int(xb))

    xr = xr[2:]
    xg = xg[2:]
    xb = xb[2:]


    if len(xr)==1:
        xr="0"+str(xr)
        num = "#" + xr+"0000"
    if len(xg)==1:
        xg = "0" + str(xg)
        num = "#" + xr + xg+"00"
    if len(xb)==1:
        xb = "0" + str(xb)
        num = "#" + xr + xg +xb
    num="#"+xr+xg+xb


    obj.config(bg=num)


s1=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s1.pack()
s2=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s2.pack()
s3=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s3.pack()
obj.config(bg='#000000')
obj.mainloop()
