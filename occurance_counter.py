import tkinter

# #MODES will allow to not have define four different radio buttons, don't neet to call it MODES
# MODES = [
#     ("pepperoni","pepperoni"),
#     ("ham","ham"),
#     ("cheese","cheese"),
#     ("mushroom","mushroom"),
# ]
#
# pizza = StringVar()
# pizza.set("pepperoni")
#
# #for loop displays corect amount of radio buttons based on array
# for text, mode in MODES:
#     Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W) #anchor = w sets Rbs to "west" meaning Left

#MODES will allow to not have define four different radio buttons, don't neet to call it MODES
MODES = [
    ("1s", 0),
    ("2s", 0),
    ("3s", 0),
    ("4s", 0),
    ("5s", 0),
    ("6s", 0),
]

dice = int
dice.set("pepperoni")

#for loop displays corect amount of radio buttons based on array
for text, mode in MODES:
    Radiobutton(root, text=text, variable=dice, value=mode).pack(anchor=W) #anchor = w sets Rbs to "west" meaning Left
