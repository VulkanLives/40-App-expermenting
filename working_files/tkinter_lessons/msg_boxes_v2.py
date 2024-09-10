from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()


root.title("Message Boxes with TKinter - Python Tkinter GUI Tutorial #13 - https://www.youtube.com/@Codemycom")
#root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("700x700")

# Other types of messagebox are: showwarning, showerror, askquestion, askokcancel, askyesno


# fucntion for pop up window
def yes_no():
    response = messagebox.askyesno("This is my popup","hello world") #first text is title of new window
    Label(root, text= response).pack()
    if response == 1:
        Label(root, text= "You clicked yes").pack()
    else:
        Label(root, text= "You clicked no").pack()

def show_error():
    response = messagebox.showerror("This is my popup","hello world") #first text is title of new window
    Label(root, text= response).pack()

def show_warning():
    response = messagebox.showwarning("This is my popup","hello world") #first text is title of new window
    Label(root, text= response).pack()

def show_info():
    response = messagebox.showinfo("This is my popup","hello world") #first text is title of new window
    Label(root, text= response).pack()


def askquestion():
    response = messagebox.askquestion("This is my popup","hello world") #first text is title of new window
    Label(root, text= response).pack()
    if response == "yes":
        Label(root, text= "You clicked yes").pack()
    else:
        Label(root, text= "You clicked no").pack()

def ask_ok_cancel():
    response = messagebox.askokcancel("This is my popup","hello world") #first text is title of new window
    Label(root, text= response).pack()
    if response == 1:
        Label(root, text= "You clicked yes").pack()
    else:
       Label(root, text= "You clicked no").pack()

Button(root, text="Yes or No popup window", command=yes_no).pack()
Button(root, text="Error popup window", command=show_error).pack()
Button(root, text="Show Warning popup window", command=show_warning).pack()
Button(root, text="show info popup window", command=show_info).pack()
Button(root, text="ask question popup window", command=askquestion).pack()
Button(root, text="ask ok cancel popup window", command=ask_ok_cancel).pack()


mainloop()