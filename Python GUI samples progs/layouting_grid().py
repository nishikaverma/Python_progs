import tkinter
obj=tkinter.Tk()
obj.geometry("600x400")

lab1=tkinter.Label(obj,text="its red   ",bg='red')
lab2=tkinter.Label(obj,text="its green ", bg="green")
lab3=tkinter.Label(obj,text="its yellow", bg="yellow")
lab4=tkinter.Label(obj,text="bye, last is blue", bg="blue")
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=0,column=1)
lab4.grid(row=1,column=1)
obj.mainloop()