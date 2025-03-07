import random
import tkinter.messagebox
import tkinter

screen=tkinter.Tk()
screen.geometry("400x300")
screen.title("Jumbled Word Game! :-D")
words=["friend", "heart", "impossible", "change", "sharing", "midnight", "dentist", "accidentally", "dictionary"]
mixiwords=["rienfd","etarh","sisimpleob","cangeh","ingahsr","nmiightd","tisted","yllatnedicca","narydictio"]
totalnumberr=9
wordo=""
score=0

def thegame():
    global wordo #justice for wordo
    wordo=random.choice(mixiwords)
    label2.config(text=wordo)

def theprotestforthecheckbutton():
    global words, score #justice for words and score
    index=mixiwords.index(wordo)
    correct=words[index]

    if correct==entry.get():
        tkinter.messagebox.showinfo("Ugh! You found me! :-(","Correct, Well Done!")
        score=score+1
        label3.config(text="Score:"+str(score)+"/9")

    else:
        tkinter.messagebox.showinfo("Ugh! You found me! :-(","Incorrect, press restart to try again.")
    mixiwords.remove(wordo)
    words.remove(correct)
    
def reset():
    global score #justice for score
    score=0

label1=tkinter.Label(screen,text="Jumbled Word Game", font=("Times New Roman", 20, "italic"))
label1.grid(row=1, column=2)

label2=tkinter.Label(screen,text="dsfd")
label2.grid(row=2, column=2)

label3=tkinter.Label(screen,text="Score: 0/9")
label3.grid(row=7, column=1)

entry=tkinter.Entry(screen)
entry.grid(row=3, column=2)

button1=tkinter.Button(screen,text="Check", command=theprotestforthecheckbutton)
button1.grid(row=5,column=2)

button2=tkinter.Button(screen,text="Reset")
button2.grid(row=6,column=2)

thegame()
screen.mainloop()