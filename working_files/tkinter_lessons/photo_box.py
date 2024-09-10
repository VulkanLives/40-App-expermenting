from tkinter import *
from PIL import ImageTk,Image #package allow use of pics

root = Tk()

root.title("Part 2 of: Using Icons, Images, and Exit Buttons - Python Tkinter GUI Tutorial #8")
#root.geometry("900x300") # set starting window size
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon




my_img1 = ImageTk.PhotoImage(Image.open("images/eli_smalle.png")) #/images is folder saved in same directory as program
my_img2 = ImageTk.PhotoImage(Image.open("images/DSCF2065.png")) #/images is folder saved in same directory as program
my_img3 = ImageTk.PhotoImage(Image.open("images/DSCF2078.png")) #/images is folder saved in same directory as program
my_img4 = ImageTk.PhotoImage(Image.open("images/DSCF2110.png")) #/images is folder saved in same directory as program
my_img5 = ImageTk.PhotoImage(Image.open("images/DSCF2110_j.jpg")) #/images is folder saved in same directory as program

image_list= [my_img1, my_img2, my_img3, my_img4, my_img5] #creates array of the images



my_img_label = Label(image=image_list[0] )
my_img_label.grid(row=2, column=0, columnspan= 3) #columnspan makes images span all columns displayed

def button_forward(img_no):
   global my_img_label
   global next_image
   global previous_image

   my_img_label.grid_forget()  # clears current image so 2 pics aen't occupying same space
   my_img_label = Label(image= image_list[img_no-1])

# alter the image number value
   button_next = Button(root, text=">>", command=lambda: button_forward(img_no + 1))
   button_previous = Button(root, text="<<", command=lambda: button_back(img_no +-1))

#If staement to detct start or images then deactive

   if img_no == 5:
      button_next = Button(root, text= ">>", state=DISABLED) #5 is the number as I know I am using 5 files


# put image on screen
   my_img_label.grid(row=2, column=0, columnspan=3)  # columnspan makes images span all columns displayed

# Repost the buttons in same position
   button_quit.grid(row= 1, column =1)
   button_previous.grid(row= 1, column =0)
   button_next.grid(row= 1, column =2)


def button_back(img_no):
    global my_img_label
    global next_image
    global previous_image

    my_img_label.grid_forget()  #clears current image so 2 pics aen't occupying same space
    my_img_label = Label(image=image_list[img_no - 1])

    # alter the image number value
    button_next = Button(root, text=">>", command=lambda: button_forward(img_no + 1))
    button_previous = Button(root, text="<<", command=lambda: button_back(img_no + -1))

    # If staement to detct start or images then deactive

    if img_no == 1:
        button_previous = Button(root, text="<<", state=DISABLED)  # 5 is the number as I know I am using 5 files

    # put image on screen
    my_img_label.grid(row=2, column=0, columnspan=3)  # columnspan makes images span all columns displayed

    # Repost the buttons in same position
    button_quit.grid(row=1, column=1)
    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)


button_quit = Button(root, text="Exit", command= root.quit) #set up quit button
button_next = Button(root, text=">>", command= lambda: button_forward(2)) #set up quit button
button_previous = Button(root, text="<<", command=lambda:button_back(1), state =DISABLED) #set up quit button


button_quit.grid(row= 1, column =1)
button_previous.grid(row= 1, column =0)
button_next.grid(row= 1, column =2)









root.mainloop()