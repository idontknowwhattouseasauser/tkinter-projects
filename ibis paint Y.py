import tkinter

class Paint():
    def __init__(self):
        self.screen=tkinter.Tk()
        self.screen.geometry("700x700")
        self.screen.title("Ibis Panit Y")
        self.penbutton=tkinter.Button(self.screen,text="Pen")
        self.penbutton.grid(row=1, column=1)
        self.eraserbutton=tkinter.Button(self.screen,text="Eraser")
        self.eraserbutton.grid(row=1, column=2)
        self.colorbutton=tkinter.Button(self.screen,text="Color")
        self.colorbutton.grid(row=1, column=3)
        self.brushbutton=tkinter.Button(self.screen,text="Brush")
        self.brushbutton.grid(row=1, column=4)
        self.thicky=tkinter.Scale(self.screen,from_=1, to= 50, orient="horizontal")
        self.thicky.grid(row=1, column=5)
        self.canvas=tkinter.Canvas(self.screen,width=700,height=650)
        self.canvas.grid(row=2,column=1,columnspan=5)
        self.screen.mainloop()

paint=Paint()