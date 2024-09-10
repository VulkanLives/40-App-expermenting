from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()

root.title("Open Files Dialog Box - Python Tkinter GUI Tutorial #15 - https://www.youtube.com/@Codemycom")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("700x700")

def open_button():
    global my_img1
    root.filename = filedialog.askopenfilename(initialdir="/tkinter_lessons/images", title="Select File", filetypes=(("png files", "*.png"), ("jpg files", "*jpg"), ("All Files", "*.*")))
    lbl1 = Label(root, text=root.filename).pack()  # this returns location, doesn actual open

    my_img1 = ImageTk.PhotoImage(Image.open(root.filename))  # /images is folder saved in same directory as program
    img_lbl = Label(image=my_img1).pack()

open_btn =Button(root, text="open a file", command=open_button).pack()

root.mainloop()