import time
import tkinter.messagebox
import tkinter

screen=tkinter.Tk()
screen.geometry("400x150")
screen.title("I'm Tiredd -_-")
screen.configure(bg='light blue')
hour=tkinter.StringVar()
minute=tkinter.StringVar()
seconds=tkinter.StringVar()
def cd():
    h=int(hour.get())
    m=int(minute.get())
    s=int(seconds.get())
    run=True
    while run:
        if h>0 and m==0 and s==0:
            h=h-1
            m=m+60
            
        if s==0:
            m=m-1
            s=s+60

        if s>0:
            s=s-1

        if h==0 and m==0 and s==0:
            run=False

        if h==0 and m==0 and s==0:
            tkinter.messagebox.showinfo("BOO! OoO","All Done, Goodbye!")
        hour.set(h)
        minute.set(m)
        seconds.set(s)
        screen.update()
        time.sleep(1)

entry=tkinter.Entry(screen,width=4,textvariable=hour)
entry.grid(row=1, column=1,pady=50,padx=25)

entry1=tkinter.Entry(screen,width=4, textvariable=minute)
entry1.grid(row=1, column=3,padx=25)

entry2=tkinter.Entry(screen,width=4, textvariable=seconds)
entry2.grid(row=1, column=5,padx=25)

label=tkinter.Label(screen,text=":")
label.grid(row=1, column=2,padx=25)

label1=tkinter.Label(screen,text=":")
label1.grid(row=1, column=4,padx=25)

button=tkinter.Button(screen,text="START NOW!",command=cd)
button.grid(row=2, column=3,padx=25)
screen.mainloop()