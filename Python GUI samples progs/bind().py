from tkinter import *
def change(e):
    obj.config(bg="red")


obj=Tk()
obj.geometry("400x400")
b=Button(obj, text="click me")
b.bind("<Button>",change)
#b.bind("<Button>",lambda e :obj.config(bg='red'))
b.pack()

obj.mainloop()