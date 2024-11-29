import tkinter

screen=tkinter.Tk()
screen.geometry("800x200")
screen.title("rps")

label=tkinter.Label(screen,text="Rock Paper Scissors",width=30,height=1)
label.grid(row=1, column=2, columnspan=2)

label3=tkinter.Label(screen,text="")
label3.grid(row=2, column=2)

label4=tkinter.Label(screen,text="Your Options:")
label4.grid(row=3, column=1)

button1=tkinter.Button(screen,text="ROCK")
button1.grid(row=4, column=2)

button2=tkinter.Button(screen,text="PAPER")
button2.grid(row=4, column=3)

button3=tkinter.Button(screen,text="SCISSORS")
button3.grid(row=4, column=4)

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