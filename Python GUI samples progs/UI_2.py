import tkinter
obj=tkinter.Tk()
obj.geometry("600x400+400+400")

lab1=tkinter.Label(obj,text="Number additon program",font="Ariel 20 bold")
lab2=tkinter.Label(obj,text="first no.")
lab3=tkinter.Label(obj,text="second no.")
e1=tkinter.Entry(obj)
e2=tkinter.Entry(obj)
b1=tkinter.Button(obj,text="Add")
b2=tkinter.Button(obj,text="Clear")
b3=tkinter.Button(obj,text="Quit")

lab1.grid(row = 0,column=0,columnspan=4)
lab2.grid(row=1,column=0)
lab3.grid(row=2,column=0)
e1.grid(row=1,column=1,columnspan=2)
e2.grid(row=2,column=1,columnspan=2)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1,sticky=tkinter.W+tkinter.E,columnspan=2)
b3.grid(row=3,column=3)

obj.mainloop()