import tkinter

screen=tkinter.Tk()
screen.geometry("400x300")
screen.title("Rainbow 0o0!")

def addition():
    e=entry.get()
    listbox.insert(tkinter.END,e)
    entry.delete(0,tkinter.END)

def deletation():
    a=listbox.curselection()
    listbox.delete(a)

def wloc(event):
    o=listbox.curselection()
    r=listbox.get(o)
    screen.config(bg=r)


button1=tkinter.Button(screen,text="DELETE", command=deletation)
button1.grid(row=1,column=2)

button3=tkinter.Button(screen,text="ADD",  command=addition)
button3.grid(row=1,column=3)

listbox=tkinter.Listbox(screen, width=50, height=10)
listbox.grid(row=3,column=2, columnspan=2)

listbox.bind("<<ListboxSelect>>",wloc)

entry=tkinter.Entry(screen, width=30)
entry.grid(row=2,column=2, columnspan=2)

screen.mainloop()