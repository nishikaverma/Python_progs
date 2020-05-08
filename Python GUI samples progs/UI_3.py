import tkinter
obj=tkinter.Tk()

msg=tkinter.StringVar()
msg.set("welcome to python!")
lab=tkinter.Label(obj,textvariable=msg,bg="red")
lab0=tkinter.Label(obj,textvariable=msg,bg="blue")
lab1=tkinter.Label(obj,textvariable=msg,bg="green")

#lab.pack(fill=tkinter.X,padx=(6,0),pady=3,side=tkinter.LEFT)
#lab0.pack(fill=tkinter.X,padx=(6,0),pady=5,side=tkinter.LEFT)
#lab1.pack(fill=tkinter.X,padx=(6,0),pady=5,side=tkinter.LEFT)

##lab.place(x=0,y=0)
#lab0.place(x=20,y=40)
#lab1.place(x=40,y=60)

obj0=tkinter.Label(obj,text="name")
obj1=tkinter.Label(obj,text="password")
obj0.grid(row=0,column=0)
obj1.grid(row=1,column=0)

obj3=tkinter.Button(obj,text="login")
obj4=tkinter.Button(obj,text="quit")
obj3.grid(row=2,column=1,sticky=tkinter.W)
obj4.grid(row=2,column=2,sticky=tkinter.E)

obj5=tkinter.Entry(obj)
obj6=tkinter.Entry(obj)
obj5.grid(row=0,column=1,columnspan=2)
obj6.grid(row=1,column=1,columnspan=2)

msg.set("hello everyone")
obj.mainloop()