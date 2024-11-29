import tkinter

screen=tkinter.Tk()
screen.geometry("600x100")
screen.title("tk")

def b1():
    e=int(entry.get())
    p=e*2.20462
    o=e*35.274
    g=e*1000
    label5.config(text=g)
    label6.config(text=p)
    label7.config(text=o)

label=tkinter.Label(screen,text="ENTER THE WEIGHT(KG)",width=30,height=1)
label.grid(row=1, column=1)

label2=tkinter.Label(screen,text="GRAM")
label2.grid(row=2, column=1)

label3=tkinter.Label(screen,text="POUND")
label3.grid(row=2, column=2)

label4=tkinter.Label(screen,text="OUNCE")
label4.grid(row=2, column=3)

label5=tkinter.Label(screen)
label5.grid(row=3, column=1)

label6=tkinter.Label(screen)
label6.grid(row=3, column=2)

label7=tkinter.Label(screen)
label7.grid(row=3, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=1, column=2)

button=tkinter.Button(screen,text="CONVERT",command=b1)
button.grid(row=1, column=3)

screen.mainloop()