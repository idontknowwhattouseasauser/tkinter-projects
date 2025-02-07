import tkinter

screen=tkinter.Tk()
screen.geometry("350x450")
screen.configure(bg='black')

def player_clicked(buttonclicked):#

    buttonclicked["text"]="X"

label=tkinter.Label(screen,text="PLAYER IS X!")
label.grid(row=1, column=2)

label1=tkinter.Label(screen,text="COMPUTER IS O!")
label1.grid(row=2, column=2)

topleft=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(topleft))
topleft.grid(row=3,column=1)

topmiddle=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(topmiddle))
topmiddle.grid(row=3, column=2)

topright=tkinter.Button(screen,text="", width=15, height=8, command=lambda:player_clicked(topright))
topright.grid(row=3, column=3)

middleleft=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(middleleft))
middleleft.grid(row=4, column=1)

middlemiddle=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(middlemiddle))
middlemiddle.grid(row=4, column=2)

middleright=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(middleright))
middleright.grid(row=4,column=3)

bottomleft=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(bottomleft))
bottomleft.grid(row=5, column=1)

bottommiddle=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(bottommiddle))
bottommiddle.grid(row=5, column=2)

bottomright=tkinter.Button(screen, text="", width=15, height=8, command=lambda:player_clicked(bottomright))
bottomright.grid(row=5, column=3)

ttt=[topleft, topmiddle, topright, middleleft, middlemiddle, middleright, bottomleft, bottommiddle, bottomright]
ap=[topleft, topmiddle, topright, middleleft, middlemiddle, middleright, bottomleft, bottommiddle, bottomright]
screen.mainloop()