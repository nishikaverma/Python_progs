from  tkinter import *
from  tkinter import messagebox

class MyGUI :
    def __init__(self,root):
        self.root=root
        self.root.geometry('400x400')
        self.lbl=Label(self.root,text='Click the button')
        self.b1=Button(self.root,text="Greet",command=self.greeting)
        self.b2= Button(self.root, text="exit", command=self.root.destroy)
        self.lbl.pack()
        self.b1.pack()
        self.b2.pack()
    def greeting(self):
        self.lbl.config(text="Hello User , Welcome to OOP GUI")


root=Tk()
obj=MyGUI(root)
root.mainloop()