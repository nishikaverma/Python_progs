from tkinter import *
from tkinter import  filedialog # 'filedialog' is a submodule of 'tkinter' module"
from tkinter import messagebox # 'messagebox' is a submodule of 'tkinter' module"

obj=Tk()
obj.geometry("400x400")
def accept():
    file_name = filedialog.askopenfilenames(filetypes=[("text", "*.txt"), ("MP3", "*.mp3"), ("image file", "*.jpg")],
                                            title="select one or more files")

    if type(file_name)==tuple:
        sr=" "
        for i in file_name:
            sr=i+'\n'
            l.config(text=sr)

'''def selection():

    file_name=filedialog.askopenfilename(filetypes=[("text","*.txt"),("MP3","*.mp3"),("image file","*.jpg")],title="select one or more files") # inables user to select any  one file,returns a string
        if len(file_name)!= 0:
            # NONE  is a value of datatype 'none type'
            messagebox.showinfo("Your selection",file_name)''' # code for selecting only one file
b=Button(obj,text="click me",command=accept)
b.pack()
l=Label(obj)
l.pack()
obj.mainloop()
