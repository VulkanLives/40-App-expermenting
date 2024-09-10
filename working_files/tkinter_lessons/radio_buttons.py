from tkinter import *
from tkinter import Label
from tkinter.ttk import Button

root = Tk()


root.title("Radio Buttons with TKinter - Python Tkinter GUI Tutorial #12")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon

r = IntVar()
r.set("2")

def clicked(value):
    debugLabel = Label(root, text=value)
    debugLabel.pack()

#"variable" refers to Tkinter's own vars to the var "1" above
Radiobutton(root, text= "Option 1", variable= r ,value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text= "Option 2", variable= r ,value=2, command=lambda: clicked(r.get())).pack()

debugLabel = Label(root, text=r.get())
debugLabel.pack()

b = Button(root, text= "Option 3", command=lambda: clicked(r.get()))
b.pack()



root.mainloop()