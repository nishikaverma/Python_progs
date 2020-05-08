import tkinter
obj=tkinter.Tk()
obj.geometry("600x400")

msg=tkinter.StringVar()
lab=tkinter.Label(obj, textvariable=msg)
lab.pack()

print(msg.get())
msg.set("hello everyone")
print(msg.get())

obj.mainloop()