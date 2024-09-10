from tkinter import *


root = Tk()

root.title("Adding Frames To Your Program - Python Tkinter GUI Tutorial #11")
#root.geometry("1000x750") # set starting window size
#root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon

frame = LabelFrame(root, text= "this is my frame....", padx=50,pady=50) #only here to show what it affects
frame.pack(padx=100 ,pady=100)

#displaying a random button, but instead of using "root"
# #we are using "frame" to make it actually go in frame specifically
button = Button(frame, text="don't click here")
button2 = Button(frame, text="or here")

#thing to not here, you can't use grid and pack when dealing with root
#but you can if use both if referring differnt bit, in this case we are reffering to labelFrame
#not root
button.grid(row = 0, column= 0)
button2.grid(row=1,column=1)

root.mainloop()