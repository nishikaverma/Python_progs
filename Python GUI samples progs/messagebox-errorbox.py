from tkinter import *
from tkinter import messagebox # 'messagebox' is a submodule of 'tkinter' module"
from tkinter import simpledialog # 'simpledialog' is a submodule of 'tkinter' module"
obj=Tk()
obj.geometry("400x400")
def div():
    try:
        e3.config(fg="green")
        num1=int(e1.get())
        num2=int(e2.get())
        sum=num1/num2
        e3.config(state=NORMAL) # enables the entry of any data inside the Entry field
        e3.delete(0, END)
        e3.insert(0,str(sum))
        e3.config(state=DISABLED) # disables the entry of any data inside the Entry field
    except ZeroDivisionError:
        messagebox.showerror("ZeroDivisionError","denominator cant be zero") # error box

    except ValueError:
        messagebox.showerror("ValueError", "only integer values are allowded") # error box


def clearit():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.focus()

def finish():
    answer=messagebox.askyesno("Question","Are  you sure you want to quit ")
    if answer==True:
        name=simpledialog.askstring("Before Going","Please enter your name...")
        if name==None or name=="":
            name="UserJee"
        messagebox.showinfo("Goodbye!", "Have a nice day %s"%name)
        sys.exit(0)

lab1=Label(obj, text="Number division program",font="Arial 22 bold")
lab2=Label(obj, text="First no.")
lab3=Label(obj,text="second no.")
lab4=Label(obj,text="result")

e1=Entry(obj)
e2=Entry(obj)
e3=Entry(obj,state=DISABLED) # disables the entry of any data inside the Entry field

b1=Button(obj, text="divide",command=div)
b2=Button(obj, text="clear",command=clearit)
b3=Button(obj, text="quit",command=finish)

lab1.grid(row=0,column=0,columnspan=4)
lab2.grid(row=1,column=0,sticky=E)
lab3.grid(row=2,column=0,sticky=E)
lab4.grid(row=3,column=0,sticky=E)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,padx=5,pady=5,sticky=E+W)
b2.grid(row=4,column=1,padx=5,pady=5,sticky=E+W)
b3.grid(row=4,column=2,padx=5,pady=5,sticky=E+W)
obj.mainloop()
