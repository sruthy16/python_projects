from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#GlobalVariables
ActivePlayer=1
player1=[]
player2=[]
root=Tk()
root.title("Tic Tac Toe : Your Move")
style=ttk.Style()
style.theme_use("classic")

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


def ButtonClicker(id):
    global ActivePlayer
    #global player1
    #global player2
    if ActivePlayer==1:
        SetLayout(id,"X")
        player1.append(id)
        root.title("Tic Tac Toe : Opponent Move")
        ActivePlayer=2
        print("PLAYER1:{}".format(player1))
    elif ActivePlayer==2:
        SetLayout(id,"O")
        player2.append(id)
        root.title("Tic Tac Toe : Your Move")
        ActivePLayer=1
        print("PLAYER2:{}".format(player2))

    CheckWinner()



def SetLayout(id,PlayerMarker):
    if id==1:
        button1.config(text=PlayerMarker)
        button1.state(["disabled"])
    elif id==2:
        button2.config(text=PlayerMarker)
        button2.state(["disabled"])
    elif id==3:
        button3.config(text=PlayerMarker)
        button3.state(["disabled"])
    elif id==4:
        button4.config(text=PlayerMarker)
        button4.state(["disabled"])
    elif id==5:
        button5.config(text=PlayerMarker)
        button5.state(["disabled"])
    elif id==6:
        button6.config(text=PlayerMarker)
        button6.state(["disabled"])
    elif id==7:
        button7.config(text=PlayerMarker)
        button7.state(["disabled"])
    elif id==8:
        button8.config(text=PlayerMarker)
        button8.state(["disabled"])
    elif id==9:
        button9.config(text=PlayerMarker)
        button9.state(["disabled"])


def CheckWinner():
    Winner=-1
    if 1 in player1 and 2 in player1 and 3 in player1:
        Winner=1
    if 1 in player2 and 2 in player2 and 3 in player2:
        Winner=2

    if 4 in player1 and 5 in player1 and 6 in player1:
        Winner=1
    if 4 in player2 and 5 in player2 and 6 in player2:
        Winner=2

    if 7 in player1 and 8 in player1 and 9 in player1:
        Winner=1
    if 7 in player2 and 8 in player2 and 9 in player2:
        Winner=2

    if 1 in player1 and 4 in player1 and 7 in player1:
        Winner=1
    if 1 in player2 and 4 in player2 and 7 in player2:
        Winner=2

    if 2 in player1 and 5 in player1 and 8 in player1:
        Winner=1
    if 2 in player2 and 5 in player2 and 8 in player2:
        Winner=2

    if 3 in player1 and 6 in player1 and 9 in player1:
        Winner=1
    if 3 in player2 and 6 in player2 and 9 in player2:
        Winner=2

    if 7 in player1 and 5 in player1 and 3 in player1:
        Winner = 1
    if 7 in player2 and 5 in player2 and 3 in player2:
        Winner = 2
    if 9 in player1 and 5 in player1 and 1 in player1:
        Winner = 1
    if 9 in player2 and 5 in player2 and 1 in player2:
        Winner = 2
    if Winner==1:
        messagebox.showinfo(title="Congratulations",message="You are the winner")
    elif Winner==2:
        messagebox.showinfo(title="Congratulations",message="Opponent is the winner")

root.mainloop()