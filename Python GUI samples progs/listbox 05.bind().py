from tkinter import *
from tkinter import simpledialog, messagebox
def show(e):
    select=lb1.curselection()
    if len(select)==0:
        messagebox.showerror("Error","please select any iten first")
    else:
        l1.config(text="your selection: " + lb1.get(select[0]))

root = Tk()
root.geometry("300x300")
l1 = Label(root, text="Your selection will appear here")
lb1 = Listbox(root)
sports = ["Cricket", "Football", "Hockey", "Basketball", "Volleyball", "Tennis", "Rugby", "Badminton", "Snooker",
          "Wrestling"]
for x in sports:
    lb1.insert(END, x)
#lb1.bind("<<ListboxSelect>>",show)
lb1.bind("<Double-Button-1>",show)
lb1.grid(row=0, column=0, sticky=W)
l1.grid(row=2, column=0, sticky=W)
root.mainloop()