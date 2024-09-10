from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()

root.title("MCreate New Windows in tKinter - Python Tkinter GUI Tutorial #1 - https://www.youtube.com/@Codemycom")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("700x700")


def openWin():
    global my_img1 #different to last this must now be global as we are using a new window
    top = Toplevel() # create new window on top
    top.title("2nd window")
    top.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
    top.geometry("700x700")
    my_img1 = ImageTk.PhotoImage(Image.open("Images/eli_smalle.png")) #/images is folder saved in same directory as program
    lbl = Label(top, image=my_img1).pack()
    close_button = Button(top, text="Close Window", command= top.destroy).pack()

button_window = Button(root, text="open 2nd window", command=openWin).pack()
close_main_button = Button(root, text="Close Window", command=root.destroy).pack()

root.mainloop()