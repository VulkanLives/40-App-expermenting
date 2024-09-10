from tkinter import * #tkinter is the GUI and the * after import gets all of it

root = Tk() # sets te route has to be first thing for it to work

myLabel = Label(root, text = "Welcome to the Dice Roller")
canvas = Canvas(root, width=400, height=300) #control the size of the window

canvas.pack()

myLabel.pack() # unsohistacated forceful text output

root.mainloop()