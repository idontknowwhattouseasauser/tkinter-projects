import tkinter

screen=tkinter.Tk()
screen.geometry("600x100")
screen.title("tk")

def b1():
    e=int(entry.get())
    e1=int(entry1.get())
    a=(e*e1)
    label4.config(text=a)
    
label=tkinter.Label(screen,text="MULTIPLYER")
label.grid(row=1, column=2)

label1=tkinter.Label(screen,text="ENTER A NUMBER:")
label1.grid(row=2, column=2)

label2=tkinter.Label(screen,text="ENTER ANOTHER NUMBER:")
label2.grid(row=3, column=2)

label3=tkinter.Label(screen,text="ANSWER:")
label3.grid(row=4, column=2)

label4=tkinter.Label(screen)
label4.grid(row=4, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=3)

entry1=tkinter.Entry(screen)
entry1.grid(row=3, column=3)

button=tkinter.Button(screen,text="MULTIPLY",command=b1)
button.grid(row=1, column=3)

screen.mainloop()