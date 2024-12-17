import time
import tkinter

screen=tkinter.Tk()
screen.geometry("700x200")

label=tkinter.Label(screen,text="hi",bg="orange",fg="white",font=("helevetica",50),width=15)
label.grid(row=1,column=1)

def showtime():
    tim=time.strftime("%H:%M:%S %p")
    label.config(text=tim)
    label.after(1000,showtime)

showtime()
screen.mainloop()