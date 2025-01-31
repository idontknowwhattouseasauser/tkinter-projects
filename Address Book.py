import tkinter.filedialog
import tkinter

screen=tkinter.Tk()
screen.geometry("500x400")
screen.title("memorizer")
info={}
def addo():
    n=entry.get()
    a=entry1.get()
    p=entry2.get()
    e=entry3.get()
    b=entry4.get()
    info[n]=[a,p,e,b]
    updatelistbox()
    entry.delete(0,tkinter.END)
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)


def updatelistbox():
    listbox.delete(0,tkinter.END)
    names=info.keys()
    for name in names:
        listbox.insert(tkinter.END,name)

def deleteo():
    idk=listbox.curselection()
    namey=listbox.get(idk)
    del info[namey]
    updatelistbox()

def edito():
    idka=listbox.curselection()
    nameya=listbox.get(idka)
    record=info[nameya]
    entry1.insert(tkinter.END,record[0])
    entry2.insert(tkinter.END,record[1])
    entry3.insert(tkinter.END,record[2])
    entry4.insert(tkinter.END,record[3])
    entry.insert(tkinter.END,nameya)

def saveo():
    file1=tkinter.filedialog.asksaveasfile()
    if file1 is not None:
        print(info,file=file1)

def openo():
    global info
    file1=tkinter.filedialog.askopenfile()
    if file1 is not None:
        info=eval(file1.read())
        updatelistbox()

label=tkinter.Label(screen,text="My Address Book:")
label.grid(row=0, column=1)

label1=tkinter.Label(screen,text="Full Name")
label1.grid(row=2, column=2)

label2=tkinter.Label(screen,text="Address")
label2.grid(row=3, column=2)

label3=tkinter.Label(screen,text="Phone")
label3.grid(row=4, column=2)

label4=tkinter.Label(screen,text="Email")
label4.grid(row=5, column=2)

label5=tkinter.Label(screen, text="Birthdate")
label5.grid(row=6, column=2)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=3)

entry1=tkinter.Entry(screen)
entry1.grid(row=3, column=3)

entry2=tkinter.Entry(screen)
entry2.grid(row=4, column=3)

entry3=tkinter.Entry(screen)
entry3.grid(row=5, column=3)

entry4=tkinter.Entry(screen)
entry4.grid(row=6, column=3)

listbox=tkinter.Listbox(screen, width=50, height=10)
listbox.grid(row=2,column=5, rowspan=5)

button=tkinter.Button(screen, text="Open", command=openo)
button.grid(row=0, column=4)

button1=tkinter.Button(screen, text="Edit", command=edito)
button1.grid(row=7, column=2)

button2=tkinter.Button(screen,  text="Delete", command=deleteo)
button2.grid(row=7, column=3)

button3=tkinter.Button(screen,  text="Update/Add",command=addo)
button3.grid(row=7, column=4)

button4=tkinter.Button(screen,text="Save", command=saveo)
button4.grid(row=8, column=2)

screen.mainloop()