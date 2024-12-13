import random
import tkinter.messagebox
import tkinter

screen=tkinter.Tk()
screen.geometry("500x400")

def ok():
   ko=entry.get()
   tkinter.messagebox.showinfo("BEAUTIFUL NAME!","Hi "+ko+",I am thinking of a number between 1-20 and you need to guess it!")

num=random.randint(1,20)
def guess():
    ko=entry.get()
    sseug=int(entry2.get())
    if sseug>num:
        tkinter.messagebox.showinfo("I AM BACK TO TELL YOU:","TOO HIGH "+ko+" ,TRY AGAIN!")

    if sseug<num:
        tkinter.messagebox.showinfo("I AM BACK TO TELL YOU:","TOO LESS "+ko+" ,TRY AGAIN!")
    
    if sseug==num:
        tkinter.messagebox.showinfo("I AM BACK TO TELL YOU:","PERFECTO "+ko+"!")

label=tkinter.Label(screen, text="WELCOME TO OUR GAME!!!")
label.grid(row=1, column=2,pady=35)

label1=tkinter.Label(screen, text="What is your name?")
label1.grid(row=2, column=1, pady=10)

entry=tkinter.Entry(screen)
entry.grid(row=3,column=1)

button=tkinter.Button(screen,text="OK",command=ok)
button.grid(row=3,column=3)

label2=tkinter.Label(screen, text="Take a guess(your opinion matters!):")
label2.grid(row=4, column=1, pady=10)

entry2=tkinter.Entry(screen)
entry2.grid(row=5,column=1)

button=tkinter.Button(screen,text="Guess", command=guess)
button.grid(row=5,column=3)

screen.mainloop()