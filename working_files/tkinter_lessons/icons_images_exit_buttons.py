from tkinter import *
from PIL import ImageTk,Image #package allow use of pics

root = Tk()

root.title("Using Icons, Images, and Exit Buttons - Python Tkinter GUI Tutorial #8")
#root.geometry("900x300") # set starting window size
root.iconbitmap("Treetog.ico") #uses an .ico file for little window Icon


button_quit = Button(root, text="Exit", command= root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("eli_smalle.png"))
#resized_img = my_img.thumbnail((500,500))
my_img_label = Label(image=my_img)

my_img_label.pack()



root.mainloop()