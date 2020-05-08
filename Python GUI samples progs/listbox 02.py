'''from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
obj=Tk()
obj.geometry("400x400")
def execute():
    enter=simpledialog.askstring("input","Enter item no.",minvalue=1,maxvalue=list.size())
    if type(enter) is int:
        item=list.get(enter-1)
        lab.config(text="your selection is: "+item)
    else:
        messagebox.showerror("Cancel Pressed!","You didn't input any value")
list=Listbox(obj,bg='yellow')
sports=["cricket","football","hockey","baseball","volliball","tanis","rugby","snooker","badminton"]
for i in sports:
    list.insert(END,i)
lab=Label(obj,text="your selected item will appear here")
b=Button(obj,text="show item",command=execute)
list.pack()
b.pack()
lab.pack()
obj.mainloop()
'''
from tkinter import *
from tkinter import simpledialog,messagebox

def show_item():
  pos=simpledialog.askinteger("Input","Enter item no",minvalue=1,maxvalue=lb1.size())
  if type(pos) is int:
    item=lb1.get(pos-1)
    l1.configure(text="You selected:"+item)
  else:
    messagebox.showinfo("Cancel Pressed!","You didn't input any value")
root = Tk()
root.geometry("300x300")
l1=Label(root,text="Your selection will appear here")
b1=Button(root,text="show item",command=show_item)
lb1=Listbox(root)
sports=["Cricket","Football","Hockey,","Basketball","Volleyball","Tennis","Rugby","Badminton","Snooker","Wrestling"]
for x in sports:
  lb1.insert(END,x)

lb1.grid(row=0,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
root.mainloop()
