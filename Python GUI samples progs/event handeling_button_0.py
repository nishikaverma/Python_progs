from tkinter import *
obj=Tk()

def redit():
    l['bg']="red"
def blueit():
    l['bg'] = "blue"
def greenit():
    l['bg'] = "green"


b1=Button(obj,text="red",command=redit)
b2=Button(obj, text="blue",command=blueit)
b3=Button(obj,text="green",command=greenit)
l=Label(obj,bg="white",width=20,height=5)

'''
# this code can also be written as:

b1=Button(obj,text="red",command=lambda:l.config(bg='red'))
b2=Button(obj, text="blue",command=lambda:l.config(bg='blue'))
b3=Button(obj,text="green",command=lambda:l.config(bg='green'))
l=Label(obj,bg="white",width=20,height=5)
'''
l.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

obj.mainloop()