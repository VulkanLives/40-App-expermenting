import random
from tkinter import *
from tkinter import Label
from tkinter.ttk import Button

root = Tk() # sets te route has to be first thing for it to work

myLabel = Label(root, text = "Welcome to the Dice Roller").pack()
canvas = Canvas(root, width=400, height=300) #control the size of the window

r = IntVar()
r.set("0")

def roll_dice(amount_of_dice):
    result_lbl = Label(root, text=amount_of_dice)
    result_lbl.pack()
    totalSum = 0
    possibleFaces = [1,2,3,4,5,6]


    for die in range(amount_of_dice):
        roll = random.choice(possibleFaces)
        totalSum += roll
        average = totalSum / amount_of_dice
        total_lbl =Label(root, text="Total sum: " + str(totalSum))
        total_lbl.pack()
        average_lbl =Label(root, text="average: " + str(average))
        average_lbl.pack()

#def clicked(value):
  #  debugLabel = Label(root, text=value)
   # debugLabel.pack()

#"variable" refers to Tkinter's own vars to the var "1" above
#Radiobutton(root, text= "1", variable= r ,value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "2", variable= r ,value=2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "3", variable= r ,value=3, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "4", variable= r ,value=4, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "5", variable= r ,value=5, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "6", variable= r ,value=6, command=lambda: clicked(r.get())).pack()

Radiobutton(root, text= "1", variable= r.set(1) , command=lambda: roll_dice(r.get())).pack()
Radiobutton(root, text= "2", variable= r.set(2) , command=lambda: roll_dice(r.get())).pack()
Radiobutton(root, text= "3", variable= r , command=lambda: roll_dice(r.get())).pack()
Radiobutton(root, text= "4", variable= r , command=lambda: roll_dice(r.get())).pack()
Radiobutton(root, text= "5", variable= r , command=lambda: roll_dice(r.get())).pack()
Radiobutton(root, text= "6", variable= r , command=lambda: roll_dice(r.get())).pack()

debugLabel = Label(root, text=r.get())
debugLabel.pack()





root.mainloop()