from tkinter import *

root = Tk()


root.title("Radio Buttons with TKinter - Python Tkinter GUI Tutorial #12 - https://www.youtube.com/@Codemycom")
root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon
root.geometry("700x700")


#MODES will allow to not have define four different radio buttons, don't neet to call it MODES
MODES = [
    ("pepperoni","pepperoni"),
    ("ham","ham"),
    ("cheese","cheese"),
    ("mushroom","mushroom"),
]

pizza = StringVar()
pizza.set("pepperoni")

#for loop displays corect amount of radio buttons based on array
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W) #anchor = w sets Rbs to "west" meaning Left

def clicked(value):
    debugLabel = Label(root, text=value)
    debugLabel.pack()

#"variable" refers to Tkinter's own vars to the var "1" above
#Radiobutton(root, text= "Option 1", variable= r ,value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "Option 2", variable= r ,value=2, command=lambda: clicked(r.get())).pack()


b = Button(root, text= "Add topping", command=lambda: clicked(pizza.get()))
b.pack()


root.mainloop()