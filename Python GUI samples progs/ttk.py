# using theamed tknter
import tkinter
import tkinter.ttk

root=tkinter.Tk()
root.geometry('400x400')

b1=tkinter.Button(root,text="the Tk() button")
b1.pack()

b2=tkinter.ttk.Button(root,text="the ttk button")
b2.pack()

root.mainloop()
