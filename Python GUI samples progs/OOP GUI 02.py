from tkinter import *
class MyGUI:
    def div(self):
        try:
            self.e3.delete(0,END)
            self.e3.config(fg="red")
            self.s3.set(int(self.s1.get())/int(self.s2.get()))

            self.e3.config(fg="green")
        except ZeroDivisionError:
            self.s3.set("denominator cant be zero!")
        except ValueError:
            self.s3.set("only numbers are allowded!")

    def clearit(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e1.focus()


    def __init__(self,obj):
        self.lab1=Label(self.obj, text="Number division program",font="Arial 22 bold")
        self.lab2=Label(self.obj, text="First no.")
        self.lab3=Label(self.obj,text="second no.")
        self.lab4=Label(self.obj,text="result")

        self.s1=StringVar()
        self.s1=StringVar()
        self.s2=StringVar()
        self.s3=StringVar()

        self.e1=Entry(self.obj,textvariable=s1)
        self.e2=Entry(self.obj,textvariable=s2)
        self.e3=Entry(self.obj,textvariable=s3)

        self.b1=Button(self.obj, text="divide",command=div)
        self.b2=Button(self.obj, text="clear",command=clearit)
        self.b3=Button(self.obj, text="quit",command=self.obj.exit(0))

        self.lab1.grid(row=0,column=0,columnspan=4)
        self.lab2.grid(row=1,column=0,sticky=E)
        self.lab3.grid(row=2,column=0,sticky=E)
        self.lab4.grid(row=3,column=0,sticky=E)
        self.e1.grid(row=1,column=1)
        self.e2.grid(row=2,column=1)
        self.e3.grid(row=3,column=1)
        self.b1.grid(row=4,column=0,padx=5,pady=5,sticky=E+W)
        self.b2.grid(row=4,column=1,padx=5,pady=5,sticky=E+W)
        self.b3.grid(row=4,column=2,padx=5,pady=5,sticky=E+W)


obj=Tk()
object=MyGUI(obj)
obj.mainloop()
