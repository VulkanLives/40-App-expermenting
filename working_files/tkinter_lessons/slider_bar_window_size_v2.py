from tkinter import *


root = Tk()

root.title("Sliders With TKinter - Python Tkinter GUI Tutorial #16 - https://www.youtube.com/@Codemycom")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("400x400")


vert_slide = Scale(root, from_= 400, to= 800)
vert_slide.pack()



def horizontal_slide():
    horiz_slide_lbl = Label(root, text= horiz_slide.get()).pack()
    root.geometry(str(horiz_slide.get())+ "x" + str(vert_slide.get()))


#create horizontal slide
horiz_slide = Scale(root, from_= 400, to= 800, orient=HORIZONTAL)
horiz_slide.pack()

horiz_slide_lbl = Label(root, text=horiz_slide.get())
horiz_slide_lbl.pack()


btn_slide_h =Button(root, text= "adjust size", command=horizontal_slide).pack()

root.mainloop()