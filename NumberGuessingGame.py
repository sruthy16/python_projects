from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

# Buttons
button1=ttk.Button(root,text=" ")
button1.grid(row=0,column=0,sticky="snew",ipadx=40,ipady=40)
button1.config(command=lambda: ButtonClicker(1))

button2=ttk.Button(root,text=" ")
button2.grid(row=0,column=1,sticky="snew",ipadx=40,ipady=40)
button2.config(command=lambda: ButtonClicker(2))

button3=ttk.Button(root,text=" ")
button3.grid(row=0,column=2,sticky="snew",ipadx=40,ipady=40)
button3.config(command=lambda: ButtonClicker(3))

button4=ttk.Button(root,text=" ")
button4.grid(row=1,column=0,sticky="snew",ipadx=40,ipady=40)
button4.config(command=lambda: ButtonClicker(4))

button5=ttk.Button(root,text=" ")
button5.grid(row=1,column=1,sticky="snew",ipadx=40,ipady=40)
button5.config(command=lambda: ButtonClicker(5))

button6=ttk.Button(root,text=" ")
button6.grid(row=1,column=2,sticky="snew",ipadx=40,ipady=40)
button6.config(command=lambda: ButtonClicker(6))

button7=ttk.Button(root,text=" ")
button7.grid(row=2,column=0,sticky="snew",ipadx=40,ipady=40)
button7.config(command=lambda: ButtonClicker(7))

button8=ttk.Button(root,text=" ")
button8.grid(row=2,column=1,sticky="snew",ipadx=40,ipady=40)
button8.config(command=lambda: ButtonClicker(8))

button9=ttk.Button(root,text=" ")
button9.grid(row=2,column=2,sticky="snew",ipadx=40,ipady=40)
button9.config(command=lambda: ButtonClicker(9))
def ButtonClicker(id) :
    print("ID:{}".format(id))

root.mainloop()