
import tkinter
# making object of Tk class present inside tkinter module, this class creates a root wedge.
tkobj=tkinter.Tk()

# to change the the default title 'tk' of the root wedge :
tkobj.title("My GUI App")

# to change the icon of root wedge: (PhotoImage is a seprate class wile iconphoto() is a method of Tk class )
img=tkinter.PhotoImage(file="D:/mypainting1.png") # it dose'nt  accepts images with jpeg extension !
tkobj.iconphoto(tkobj,img)

# to change the size of root window(600x400) and to change the location of apperiance of root window(+300+250):
tkobj.geometry("600x400+300+250")

# to set the root window at the center of the screen:
sw=tkobj.winfo_screenwidth() # to get the width of desktop screen
sh=tkobj.winfo_screenheight() # to get the height of desktop screen
width=sw//2
height=sh//2
xco=sw//4
yco=sh//4
tkobj.geometry(f"{width}x{height}+{xco}+{yco}")

# to restrict the resizing of root window:
tkobj.resizable(False,False)

tkobj.mainloop() # this method displays the root wedge through an infinite loop until the root wedge is not closed

