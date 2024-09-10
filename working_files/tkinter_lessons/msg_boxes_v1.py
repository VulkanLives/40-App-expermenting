from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()


root.title("Message Boxes with TKinter - Python Tkinter GUI Tutorial #13 - https://www.youtube.com/@Codemycom")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("700x700")

# Other types of messagebox are: showwarning, showerror, askquestion, askokcancel, askyesno


# fucntion for pop up window
def popup():
    messagebox.showinfo("This is my popup","hello world") #first text is title of new window

def popupWarn():
    messagebox.showwarning("This is my popup","hello world") #first text is title of new window


Button(root, text="Popup", command=popup).pack()
Button(root,text="warning", command=popupWarn).pack()

mainloop()