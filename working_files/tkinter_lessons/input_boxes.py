from tkinter import * #tkinter is the GUI and the * after import gets all of it

root = Tk() # sets te route has to be first thing for it to work
root.geometry("700x300") # set starting window size

e = Entry(root, width = 50)
e.grid(row=40, column=20)


def buttonClick():
#creating instances of buttons and label and canvas etc
    confirmationClick = Label(root, text= e.get()) #takes user entry
    confirmationClick.grid(row=25, column=20)

def buttonClick2():
#creating instances of buttons and label and canvas etc
    hello = "Hello " + e.get()
    confirmationClick = Label(root, text= hello) #takes user entry
    confirmationClick.grid(row=25, column=20)


button = Button(root, text= "enter your name", command=buttonClick, fg=("blue"), bg=("red")) #"command" makes the calls the above function, fg is text colour "foreground" and Bg = background
# print the items from the above into window
button.grid(row=30, column=20) # same methid for creating this button

button2 = Button(root, text= "enter your name", command=buttonClick2, fg=("blue"), bg=("red")) #"command" makes the calls the above function, fg is text colour "foreground" and Bg = background
# print the items from the above into window
button2.grid(row=31, column=20) # same methid for creating this button


root.mainloop()