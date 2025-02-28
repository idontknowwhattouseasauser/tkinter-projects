import tkinter.messagebox
import tkinter

screen=tkinter.Tk()
screen.geometry("600x400")
screen.title("calcalator")
screen.configure(bg="grey")

def b1():
    e=int(entry.get())
    e1=int(entry1.get())
    e2=entry2.get()
    if e2=="+":
        f=(e+e1)
        label3.config(text=f)

    elif e2=="-":
        f=(e-e1)
        label3.config(text=f)

    elif e2=="*":
        f=(e*e1)
        label3.config(text=f)

    elif e2=="/":
        f=(e/e1)
        label3.config(text=f)

    else:
        tkinter.messagebox.showinfo("ERROR","That is not possible!")


label=tkinter.Label(screen,text="What do you want for the first number? (1-10):",bg="gray")
label.grid(row=1, column=1)

label1=tkinter.Label(screen,text="What do you want for the second number? (1-10):",bg="grey")
label1.grid(row=2, column=1)

label2=tkinter.Label(screen,text="What do you want to do? either +,-,*,/",bg="gray")
label2.grid(row=3, column=1)

label3=tkinter.Label(screen,text="",bg="gray")
label3.grid(row=4, column=1)

entry=tkinter.Entry(screen)
entry.grid(row=1, column=3)

entry1=tkinter.Entry(screen)
entry1.grid(row=2, column=3)

entry2=tkinter.Entry(screen)
entry2.grid(row=3, column=3)

button=tkinter.Button(screen, text="calculate", command=b1)
button.grid(row=4, column=2)

screen.mainloop()