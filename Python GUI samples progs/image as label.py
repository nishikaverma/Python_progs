import tkinter
obj=tkinter.Tk()
obj.geometry("600x400")
img=tkinter.PhotoImage(file="D:/img1.png")
lab=tkinter.Label(obj,text="ISRO",image=img, compound=tkinter.LEFT)
lab.pack()
obj.mainloop()