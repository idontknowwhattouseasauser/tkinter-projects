import tkinter.ttk
import tkinter

screen=tkinter.Tk()
screen.geometry("1000x300")
screen.configure(bg='Red')
screen.title("Welcome to Pizza Hut!")
pizza=["Veg Extravaganza","Magarita","Hawaiian","Meatlovers","Deep Dish","Ham, Ham, Hooray!","Diablo","BBQ Banter","Italiano","New York' Style","Four Cheese","Triple Peproni"]
qnl=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

def b1():
    e=str(cb.get())
    e1=str(cb1.get())
    e2=str(rbsv.get())
    label3.config(text="You ordered,"+e1+" size "+e2+" "+e+"/s")
label=tkinter.Label(screen,text="Type?:", bg="red",fg="white",font=("courier",25))
label.grid(row=1, column=1)

label2=tkinter.Label(screen,text="Quantiy?:", bg="red",fg="white",font=("courier",25))
label2.grid(row=2, column=1)

label3=tkinter.Label(screen,text="---", bg="red",fg="white",font=("courier",20))
label3.grid(row=6, column=2)
button=tkinter.Button(screen,text="Order", command=b1)
button.grid(row=4, column=3, columnspan=1)

cb=tkinter.ttk.Combobox(screen)
cb["values"]=pizza
cb.grid(row=1,column=2)

cb1=tkinter.ttk.Combobox(screen)
cb1["values"]=qnl
cb1.grid(row=2,column=2)

rbsv=tkinter.StringVar()

rb=tkinter.Radiobutton(screen,text="S",variable=rbsv,value="small")
rb.grid(row=2,column=5)

rb1=tkinter.Radiobutton(screen,text="M",variable=rbsv,value="MeDIuM")
rb1.grid(row=3,column=5)

rb2=tkinter.Radiobutton(screen,text="L",variable=rbsv,value="LARGE")
rb2.grid(row=4,column=5)

screen.mainloop()