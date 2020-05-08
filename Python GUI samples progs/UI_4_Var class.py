from tkinter import *
obj=Tk()
obj.geometry("400x400")
def div():
    try:
        e3.delete(0,END)
        e3.config(fg="red")
        #num1=s1.get()
        #num2=s2.get()
        #sum=num1/num2
        s3.set(int(s1.get())/int(s2.get()))

        e3.config(fg="green")
    except ZeroDivisionError:
        s3.set("denominator cant be zero!")
    except ValueError:
        s3.set("only numbers are allowded!")

def clearit():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.focus()

def finish():

    sys.exit(0)

lab1=Label(obj, text="Number division program",font="Arial 22 bold")
lab2=Label(obj, text="First no.")
lab3=Label(obj,text="second no.")
lab4=Label(obj,text="result")

s1=StringVar()
s2=StringVar()
s3=StringVar()

e1=Entry(obj,textvariable=s1)
e2=Entry(obj,textvariable=s2)
e3=Entry(obj,textvariable=s3)

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
