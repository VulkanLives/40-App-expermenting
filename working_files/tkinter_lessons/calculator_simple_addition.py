from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 50)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#click event function
def button_click(number):
    current = e.get()
    e.delete(0, END) #clears e
    e.insert(0, str(current) + str(number))

#button to make clear button clear numbers
def button_clear():
    e.delete(0, END)  # clears e

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

#notes before next lesson, this will only work for simple addition
# Equals button will need to what to do with the numbers instead of just adding
#my theory before looking at lesson would be for the add/minus/divide/etc buttons to set a flag/global var
#that will tell the program as a whole what condition is active
#so "def button_equals" will check that and behave appropriately via if statement
def button_equals():
    second_number = e.get() # would be better to update a global var with current result to do multiple actions
    e.delete(0,END)
    e.insert(0, f_num + int(second_number))





#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command= button_add)
button_minus = Button(root, text="-", padx=39, pady=20, command=lambda: button_click())
button_divide = Button(root, text="/", padx=39, pady=20, command=lambda: button_click())
button_multiply = Button(root, text="x", padx=39, pady=20, command=lambda: button_click())
button_clear = Button(root, text="CLR", padx=39, pady=20, command= button_clear) # don't need lamba as we aren't giving anything
button_equals = Button(root, text="=", padx=91, pady=20, command= button_equals)

#putbuttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=6, column =0)
button_minus.grid(row=2, column =3)
button_divide.grid(row=3, column =3)

button_multiply.grid(row=4, column =3)
button_add.grid(row=1, column =3)
button_equals.grid(row=4, column =1, columnspan=2)


root.mainloop()

