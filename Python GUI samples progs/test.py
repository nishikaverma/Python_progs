from tkinter import *

obj=Tk()
obj.geometry("400x400")
def callR(xr):
    xr=hex(int(xr))
    xr=xr[2:]
    if len(xr)==1:
        xr="0"+str(xr)
    num = "#" + str(xr) + "0000"
    obj.config(bg=num)
    return xr
def callG(xg):
    xg=hex(int(xg))
    xg=xg[2:]

    if len(xg)==1:
        xg="0"+str(xg)
    num = "#" + callR(s1.get()) +str(xg) + "00"
    obj.config(bg=num)
    return xg
def callB(xb):
    xb=hex(int(xb))
    xb = xb[2:]
    if len(xb) == 1:
        xb = "0" + str(xb)
    num = "#"+callR(s1.get()) +callG(s2.get())+ str(xb)
    obj.config(bg=num)


s1=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=callR)
s1.pack()
s2=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=callG)
s2.pack()
s3=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=callB)
s3.pack()
obj.config(bg='#000000')
obj.mainloop()
