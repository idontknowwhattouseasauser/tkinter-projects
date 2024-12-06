import tkinter

screen=tkinter.Tk()
screen.geometry("600x100")
screen.title("tk")

def b1():
    e=int(entry.get())
    f=((e*9/5)+32)
    label3.config(text=f)
    
label=tkinter.Label(screen,text="Celsius -> Fahrenheit")
label.grid(row=1, column=2)

label1=tkinter.Label(screen,text="ENTER THE TEMPRATURE IN CELSIUS",width=30,height=1)
label1.grid(row=2, column=2)

label2=tkinter.Label(screen,text="TEMPRATURE IN FAHRENHEIT")
label2.grid(row=3, column=2)

label3=tkinter.Label(screen)
label3.grid(row=3, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=3)

button=tkinter.Button(screen,text="CONVERT",command=b1)
button.grid(row=1, column=3)

screen.mainloop()