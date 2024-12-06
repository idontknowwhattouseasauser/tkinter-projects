import random
import tkinter

screen=tkinter.Tk()
screen.geometry("800x200")
screen.title("rps")
csc=0
ysc=0
choices=["rock","scissors","paper"]
def bittin(userselection):
    global csc, ysc
    comp=random.choice(choices)
    label6.config(text="Computer Selected: "+comp)
    label8.config(text="You Selected: "+userselection)

    if comp=="rock" and userselection=="scissors":
        csc=csc+1

    if comp==userselection:
        csc=csc+0
        ysc=ysc+0

    label7.config(text="Computer Score: "+csc)
    label9.config(text="Your Score: "+ysc)


label=tkinter.Label(screen,text="Rock Paper Scissors",width=30,height=1)
label.grid(row=1, column=2, columnspan=2)

label3=tkinter.Label(screen,text="")
label3.grid(row=2, column=2)

label4=tkinter.Label(screen,text="Your Options:")
label4.grid(row=3, column=1)

button1=tkinter.Button(screen,text="ROCK", command=lambda:bittin("rock"))
button1.grid(row=4, column=2)

button2=tkinter.Button(screen,text="PAPER", command=lambda:bittin("paper"))
button2.grid(row=4, column=3)

button3=tkinter.Button(screen,text="SCISSORS", command=lambda:bittin("scissors"))
button3.grid(row=4, column=4,padx=40)

label5=tkinter.Label(screen,text="Score:")
label5.grid(row=5, column=1)

label6=tkinter.Label(screen,text="You Selected:")
label6.grid(row=6, column=2)

label7=tkinter.Label(screen,text="Player Score")
label7.grid(row=6, column=3)

label8=tkinter.Label(screen,text="Computer Selected:")
label8.grid(row=7, column=2)

label9=tkinter.Label(screen,text="Computer Score")
label9.grid(row=7, column=3)

screen.mainloop()