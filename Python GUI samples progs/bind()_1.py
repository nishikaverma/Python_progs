from tkinter import *
def change1(e):
    obj.config(bg="red")

def change2(e):
    obj.config(bg="green")

obj=Tk()
obj.geometry("400x400")
b=Button(obj, text="click me")
b.bind("<Button-1>",change1)
#b.bind("<Button-1>",lambda e:obj.config(bg='red'))
b.bind("<Button-3>",change2)
#b.bind("<Button-3>",lambda e:obj.config(bg='green'))
b.pack()

obj.mainloop()