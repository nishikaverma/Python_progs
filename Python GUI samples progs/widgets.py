import tkinter
import tkinter.font
obj=tkinter.Tk()
# creating label
lab=tkinter.Label(obj,text="Python Rocks!", borderwidth=8 ,height= 3,anchor="n",relief="sunken", font="Times 22 bold", bg="yellow", fg="white", width=30)# unit of width=text unit
lab.pack() # adding label to root window

print(lab.keys()) # to get the list of all attributes that can be give to label

print(lab['bg'])
lab['fg']="green"

lab.configure(bg="red") # to to change the label settings after creating label

fobj=tkinter.font.Font(weight="bold")

obj.configure(bg="#00f",width=40) # to change the properties of root window after creating the widgets


obj.geometry("600x200")
obj.mainloop()