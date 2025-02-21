import tkinter

screen=tkinter.Tk()
screen.geometry("600x400")
screen.title("calcalator")
screen.configure(bg="grey")

label=tkinter.Label(screen,text="What do you want for the first number?:",bg="gray")
label.grid(row=1, column=1)

label1=tkinter.Label(screen,text="What do you want for the second number?:",bg="grey")
label1.grid(row=1, column=2)

label2=tkinter.Label(screen,text="What do you want to do? either +,-,*,/",bg="gray")
label2.grid(row=1, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=1, column=2)

entry1=tkinter.Entry(screen)
entry1.grid(row=2, column=3)

entry2=tkinter.Entry(screen)
entry2.grid(row=1, column=4)

screen.mainloop()