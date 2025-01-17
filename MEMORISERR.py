import tkinter.filedialog
import tkinter.ttk
import tkinter

screen=tkinter.Tk()
screen.geometry("400x300")
screen.configure(bg='pink')
screen.title("memorizer")

def addition():
    e=entry.get()
    listbox.insert(tkinter.END,e)
    entry.delete(0,tkinter.END)

def deletation():
    a=listbox.curselection()
    listbox.delete(a)

def savation():
    file1=tkinter.filedialog.asksaveasfile()
    if file1 is not None:
        for item in listbox.get(0,tkinter.END):
            print(item,file=file1)

def opentation():
    file1=tkinter.filedialog.askopenfile()
    if file1 is not None:
        items=file1.readlines()
        for item in items:
            listbox.insert(tkinter.END,item)
button=tkinter.Button(screen,text="OPEN", padx=10, pady=10,command=opentation)
button.grid(row=1,column=1)

button1=tkinter.Button(screen,text="DELETE", padx=10, pady=10, command=deletation)
button1.grid(row=1,column=2)

button2=tkinter.Button(screen,text="SAVE", padx=10, pady=10, command=savation)
button2.grid(row=1,column=3)

button3=tkinter.Button(screen,text="ADD", padx=10, pady=10, command=addition)
button3.grid(row=2,column=3)

entry=tkinter.Entry(screen, width=30)
entry.grid(row=2,column=1, columnspan=2)

listbox=tkinter.Listbox(screen, width=50, height=10)
listbox.grid(row=3,column=1, columnspan=3)

screen.mainloop()