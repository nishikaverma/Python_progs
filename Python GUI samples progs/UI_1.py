import tkinter
obj=tkinter.Tk()
obj.geometry("600x400+400+400")

lab1=tkinter.Label(obj,text=" Username")
lab2=tkinter.Label(obj,text="password")
e1=tkinter.Entry(obj)
e2=tkinter.Entry(obj)
b1=tkinter.Button(obj,text="login")
b2=tkinter.Button(obj,text="quit")
c1=tkinter.Checkbutton(obj,text="keep me log in")

lab1.grid(row = 0,column=0)
lab2.grid(row=1,column=0)
e1.grid(row=0,column=1,columnspan=2)
e2.grid(row=1,column=1,columnspan=2)
c1.grid(row=2,column=1,columnspan=2,sticky=tkinter.W)
b1.grid(row=3,column=1,sticky=tkinter.W+tkinter.E)
b2.grid(row=3,column=2,sticky=tkinter.W+tkinter.E)

obj.mainloop()