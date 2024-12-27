import tkinter

screen=tkinter.Tk()
screen.geometry("800x200")
screen.title("tk")

def b1():
    e=int(entry.get())
    e1=int(entry1.get())
    e2=str(entry2.get())
    if e2=="+":
        a=(e+e1)

    elif e2=="-":
        a=(e-e1)

    elif e2=="*":
        a=(e*e1)

    elif e2=="/":
        a=(e/e1)
        
    label4.config(text=a)
    
label=tkinter.Label(screen,text="CALCULATOR",font=("Monospace",50))
label.grid(row=1, column=2)

label1=tkinter.Label(screen,text="ENTER A NUMBER:")
label1.grid(row=2, column=2)

label2=tkinter.Label(screen,text="ENTER ANOTHER NUMBER:")
label2.grid(row=3, column=2)

label5=tkinter.Label(screen,text="+,-,* or /?")
label5.grid(row=4, column=2)

label3=tkinter.Label(screen,text="ANSWER:")
label3.grid(row=2, column=4)

label4=tkinter.Label(screen)
label4.grid(row=2, column=5)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=3)

entry1=tkinter.Entry(screen)
entry1.grid(row=3, column=3)

entry2=tkinter.Entry(screen)
entry2.grid(row=4, column=3)

button=tkinter.Button(screen,text="MULTIPLY",command=b1)
button.grid(row=1, column=3)

screen.mainloop()