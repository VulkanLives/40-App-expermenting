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
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    second_number = e.get() # would be better to update a global var with current result to do multiple actions
    e.delete(0,END)

    # if statements to determine action
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtract":
        e.insert(0, f_num - int(second_number))

    if math == "divide":
            e.insert(0, f_num / int(second_number))

    if math == "multiply":
        e.insert(0, f_num * int(second_number))


def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)



#define number buttons using lambda to a String even though it is an integer
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

#define operator buttons, don't need Lambda for this
button_add = Button(root, text="+", padx=39, pady=20, command= button_add)
button_minus = Button(root, text="-", padx=39, pady=20, command= button_minus)
button_divide = Button(root, text="/", padx=39, pady=20, command=button_divide)
button_multiply = Button(root, text="x", padx=39, pady=20, command= button_multiply)
button_clear = Button(root, text="CLR", padx=34, pady=20, command= button_clear) # don't need lamba as we aren't giving anything
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

