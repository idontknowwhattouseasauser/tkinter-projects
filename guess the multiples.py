import random
import tkinter.messagebox
import tkinter

screen=tkinter.Tk()
screen.geometry("600x100")
screen.title("tk")
n=random.randint(1,12)
nu=random.randint(1,12)
def b1():
    global n,nu
    e=int(entry.get())
    if e==n*nu:
        tkinter.messagebox.showinfo("Hello!","You are right!")
        screen.destroy()

    else:
        tkinter.messagebox.showinfo("Hello!","You are wrong! Try Again!")


def numerals():
    global n,nu
    labelnum.config(text=n)

label=tkinter.Label(screen,text="MULTIPLYER")
label.grid(row=1, column=2)

label1=tkinter.Label(screen,text="GUESS THE MULTIPLE:")
label1.grid(row=2, column=2)

label2=tkinter.Label(screen,text="THE PRODUCT:")
label2.grid(row=3, column=2)

label3=tkinter.Label(screen,text="NUMBER ONE!:")
label3.grid(row=4, column=2)

label4=tkinter.Label(screen)
label4.grid(row=4, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=3)

labelnum=tkinter.Label(screen)
labelnum.grid(row=4, column=3)

button=tkinter.Button(screen,text="MULTIPLY",command=b1)
button.grid(row=1, column=3)

numerals()

screen.mainloop()