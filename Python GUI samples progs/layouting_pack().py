import tkinter
obj=tkinter.Tk()
obj.geometry("600x400")
lab1=tkinter.Label(obj,text="hello everone",bg='red')
lab2=tkinter.Label(obj,text="I am here...", bg="green")
lab3=tkinter.Label(obj,text="nice to see you", bg="yellow")
lab4=tkinter.Label(obj,text="bye", bg="blue")

lab1.pack(fill=tkinter.X,padx=50,pady=30,ipadx=20, side=tkinter.LEFT)
lab2.pack(fill=tkinter.Y,padx=50,pady=30,ipadx=30,side=tkinter.LEFT)
lab3.pack(fill=tkinter.X,padx=(50,80),pady=30,side=tkinter.LEFT)
lab4.pack(fill=tkinter.BOTH, padx=(80,0),pady=30,side=tkinter.LEFT)
obj.mainloop()