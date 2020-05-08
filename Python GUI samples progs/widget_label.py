import tkinter
import tkinter.font

obj=tkinter.Tk()
fobj=tkinter.font.Font(weight="normal")

obj.geometry("600x400")

# creating a labels:
lab1=tkinter.Label(obj,text="Hello everyone!!", bg="red",fg="blue", font="Arise 24 italic",width="30", height='4',borderwidth=8, relief="sunken",anchor="center")
lab1.pack()

lab2=tkinter.Label(obj,text="I am back...", font=fobj, borderwidth=8, relief="ridge")
lab2.pack()

# to change the properties of a label after its creation :
lab1.config(bg="yellow")
lab2.configure(fg="#0f0",bg="#00f", font=("Times New Roman",24,"bold underline"))

img=tkinter.PhotoImage(file="F:/mypainting2.png")
lab3=tkinter.Label(obj,image=img,text="welcome to python",compound=tkinter.LEFT)
lab3.pack()

obj.config(bg="red")

obj.mainloop()
