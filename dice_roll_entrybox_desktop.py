import random
from tkinter import *

root = Tk()

root.title("Welcome to the dice roller")
root.geometry("400x600+900+900") # sets size i firstnumberxnumber and seccond sets window to right  hand size



e = Entry(root, width = 10)
e.grid(row=40, column=20, )
e.focus()



def button_click2():
#creating instances of buttons and label and canvas etc
    user_input = e.get() #get user input,will be as string
    amount_of_dice = int(user_input) #convert user string into int

    rollDice(amount_of_dice) #call roll function and pass it number entered by user

def rollDice(number):
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6] # set possible dice results
  result_list = [] # initialise empty array

  for die in range(number):
    roll = random.choice(possibleFaces) #roll a dice
    result_list.append(roll) # add dice result to array
    totalSum += roll
    average = totalSum / number


  print("Total sum: ", totalSum)
  print("Average roll: ", average)
  print(result_list)


button2 = Button(root, text= "Roll Dice", command=button_click2) #"command" makes the calls the above function, fg is text colour "foreground" and Bg = background
# print the items from the above into window
button2.grid(row=31, column=20) # same methid for creating this button


root.mainloop()