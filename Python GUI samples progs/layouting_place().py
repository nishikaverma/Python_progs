import tkinter
obj=tkinter.Tk()
obj.geometry("600x400")

lab1=tkinter.Label(obj,text="its  red",bg='red')
lab2=tkinter.Label(obj,text="its green", bg="green")
lab3=tkinter.Label(obj,text="its yellow", bg="yellow")
lab4=tkinter.Label(obj,text="bye, last is blue", bg="blue")
lab1.place(x=0,y=0)# x and y are in pixals
lab2.place(x=40,y=40)
lab3.place(x=40,y=80)
lab4.place(x=80,y=100)
obj.mainloop()