import tkinter.ttk
import tkinter

screen=tkinter.Tk()
screen.geometry("500x500")
screen.title("Hey! You found me! o^o")
cbnl=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def bittin():
    ecb=int(cb.get())
    erb=int(rbsv.get())
    print(ecb)
    print(erb)

label=tkinter.Label(screen,text="MULTIPLICATION TABLE",font=("courier",25))
label.grid(row=1, column=1, columnspan=3)

label1=tkinter.Label(screen,text="Choose:")
label1.grid(row=2,column=1)

cb=tkinter.ttk.Combobox(screen)
cb["values"]=cbnl
cb.grid(row=2,column=2)

rbsv=tkinter.IntVar()

rb=tkinter.Radiobutton(screen,text=10,variable=rbsv,value=10)
rb.grid(row=2,column=5)

rb1=tkinter.Radiobutton(screen,text=20,variable=rbsv,value=20)
rb1.grid(row=3,column=5)

rb2=tkinter.Radiobutton(screen,text=30,variable=rbsv,value=30)
rb2.grid(row=4,column=5)

button=tkinter.Button(screen,text="TABLEIZE!",command=bittin)
button.grid(row=3,column=2)

label2=tkinter.Label(screen)
label2.grid(row=4, column=2)
screen.mainloop()