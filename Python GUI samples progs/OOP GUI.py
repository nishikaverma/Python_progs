from  tkinter import *
from  tkinter import messagebox

class MyGUI :
    def __init__(self,root):

        self.root=root
        self.root.geometry('200x200')
        self.root.title=("my app")
        self.root.lab=Label(self.root,text="")
        self.root.b1=Button(self.root,text="click me",command=self.msg)
        self.root.b1.pack()
        self.root.lab.pack()
        self.count=0


    def msg(self):

        self.count=self.count+1
        self.root.lab.config(text=self.count)


root=Tk()
obj=MyGUI(root)
root.mainloop()