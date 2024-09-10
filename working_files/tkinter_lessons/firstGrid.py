from tkinter import * #tkinter is the GUI and the * after import gets all of it

root = Tk() # sets te route has to be first thing for it to work

#creating instances of buttons and label and canvas etc
myLabel = Label(root, text = "Welcome to the Dice Roller")
myLabel1 = Label(root, text = "Label using Grid")
button = Button(root, text= "click me")
canvas = Canvas(root, width=400, height=300) #control the size of the window

# print the items from the above into window
myLabel.grid(row=20, column=20)
myLabel1.grid(row=21, column=20)  # by using .grid, we specify postion instean of using .pack
button.grid(row=30, column=20) # same methid for creating this button




root.mainloop()