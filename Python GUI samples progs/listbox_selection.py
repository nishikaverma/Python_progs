from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
obj=Tk()
obj.geometry("400x400")
def execute():
    enter=li.curselection()
    if len(enter) is not 0:
        str=''
        for x in enter:
            item=li.get(x)
            str+=item+'\n'

        lab.config("you entered:"+str)
    else:
        messagebox.showerror("error","please select any item")
li=Listbox(obj,bg='yellow',selectmode=MULTIPLE)
sports=["cricket","football","hockey","baseball","volliball","tanis","rugby","snooker","badminton"]
for i in sports:
    li.insert(END,i)
lab=Label(obj,text="your selected item will appear here")
b=Button(obj,text="show item",command=execute)
li.pack()
b.pack()
lab.pack()
obj.mainloop()