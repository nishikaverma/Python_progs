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


    xr_sliced=xr[2:]
    if len(xr_sliced)==1:
        num="#0"+str(xr_sliced)+"0000"
    else:
        num = "#" + str(xr_sliced) + "0000"
    obj.config(bg=num)



    xg_sliced = xg[2:]
    if len(xr_sliced) != 1:
        if len(xg_sliced) == 1:
            num = "#" +str(xr_sliced)+"0"+ str(xg_sliced) + "00"
        else:
            num = "#" +str(xr_sliced)+ str(xg_sliced) + "00"
    else:
        if len(xg_sliced) == 1:
            num = "#0" +str(xr_sliced)+"0"+ str(xg_sliced) + "00"
        else:
            num = "#0" +str(xr_sliced)+ str(xg_sliced) + "00"

    obj.config(bg=num)



    xb_sliced = xb[2:]
    if len(xr_sliced) != 1:
        if len(xg_sliced) != 1:
            if len(xb_sliced) == 1:
                num = "#" + str(xr_sliced)+ str(xg_sliced) + '0'+ str(xb_sliced)
            else:
                num = "#" + str(xr_sliced) + str(xg_sliced) +  str(xb_sliced)
        else:
            if len(xb_sliced) == 1:
                num = "#" + str(xr_sliced)+"0"+ str(xg_sliced) + '0'+ str(xb_sliced)
            else:
                num = "#" + str(xr_sliced) +'0'+ str(xg_sliced) +  str(xb_sliced)
    else:
        if len(xg_sliced) != 1:
            if len(xb_sliced) == 1:
                num = "#0" + str(xr_sliced)+ str(xg_sliced) + '0'+ str(xb_sliced)
            else:
                num = "#0" + str(xr_sliced) + str(xg_sliced) +  str(xb_sliced)
        else:
            if len(xb_sliced) == 1:
                num = "#0" + str(xr_sliced)+"0"+ str(xg_sliced) + '0'+ str(xb_sliced)
            else:
                num = "#0" + str(xr_sliced) +'0'+ str(xg_sliced) +  str(xb_sliced)
    obj.config(bg=num)


s1=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s1.pack()
s2=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s2.pack()
s3=Scale(obj,from_=0,to=255,orient=HORIZONTAL,command=call)
s3.pack()
obj.config(bg='#000000')
obj.mainloop()
