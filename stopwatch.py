import tkinter

screen=tkinter.Tk()
screen.geometry("400x150")
screen.title("I'm Tiredd -_-")

entry=tkinter.Entry(screen,width=4)
entry.grid(row=1, column=1,pady=50,padx=25)

entry1=tkinter.Entry(screen,width=4)
entry1.grid(row=1, column=3,padx=25)

entry2=tkinter.Entry(screen,width=4)
entry2.grid(row=1, column=5,padx=25)

label=tkinter.Label(screen,text=":")
label.grid(row=1, column=2,padx=25)

label1=tkinter.Label(screen,text=":")
label1.grid(row=1, column=4,padx=25)

button=tkinter.Button(screen,text="START NOW!")
button.grid(row=2, column=3,padx=25)
screen.mainloop()