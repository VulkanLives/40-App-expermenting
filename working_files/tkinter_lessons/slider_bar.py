from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()

root.title("Sliders With TKinter - Python Tkinter GUI Tutorial #16 - https://www.youtube.com/@Codemycom")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("700x700")

#create vertical slide
slide1 = Scale(root, from_= 1, to= 10)
slide1.pack()

#create horizontal slide
slide2 = Scale(root, from_= 1, to= 10, orient=HORIZONTAL)
slide2.pack()

def vertical_slide():
    slide1_lbl = Label(root, text=slide1.get()).pack()

def horizontal_slide():
    slide2_lbl = Label(root, text= slide2.get()).pack()

btn_slide_v =Button(root, text= "Read vert slide", command=vertical_slide).pack()
btn_slide_h =Button(root, text= "Read horiz slide", command=horizontal_slide).pack()

root.mainloop()