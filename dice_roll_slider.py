from tkinter import *
import random

root = Tk()

root.title("Dice Roller")
root.geometry("400x400")

e = Entry(root, width = 10)
e.grid(row=40, column=20)
e.focus()

#create horizontal slide
horiz_slide = Scale(root, from_= 1, to= 40, orient=HORIZONTAL)
horiz_slide.grid()

horiz_slide_lbl = Label(root, text=horiz_slide.get())
horiz_slide_lbl.grid()


def horizontal_slide():
    horiz_slide_lbl = (Label(root, text= str(horiz_slide.get)))
    horiz_slide_lbl.grid(row = 3, column =3)
    user_input = e.get() # get user input,will be as string
    amount_of_dice = int(user_input)  # convert user string into int
    rollDice(amount_of_dice)  # call roll function and pass it number entered by user

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



btn_slide_h =Button(root, text= "Roll Dice", command=horizontal_slide).grid()
root.mainloop()