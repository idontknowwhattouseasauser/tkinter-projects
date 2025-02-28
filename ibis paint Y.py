from tkinter.colorchooser import askcolor
import tkinter

class Paint():
    def __init__(self):
        self.screen=tkinter.Tk()
        self.screen.geometry("700x700")
        self.screen.title("Ibis Panit Y")
        self.penbutton=tkinter.Button(self.screen,text="Pen", command=self.pen)
        self.penbutton.grid(row=1, column=1)
        self.eraserbutton=tkinter.Button(self.screen,text="Eraser", command=self.eraser)
        self.eraserbutton.grid(row=1, column=2)
        self.colorbutton=tkinter.Button(self.screen,text="Color", command=self.color)
        self.colorbutton.grid(row=1, column=3)
        self.brushbutton=tkinter.Button(self.screen,text="Brush", command=self.brush)
        self.brushbutton.grid(row=1, column=4)
        self.thicky=tkinter.Scale(self.screen,from_=1, to= 50, orient="horizontal")
        self.thicky.grid(row=1, column=5)
        self.canvas=tkinter.Canvas(self.screen,width=700,height=650)
        self.canvas.grid(row=2,column=1,columnspan=5)
        self.set_up()
        self.screen.mainloop()
    def set_up(self):
        self.color="black"
        self.size=10
        self.activebutton=self.penbutton
        self.eraser_on=False
        self.canvas.bind("<B1-Motion>",self.draw)
        self.canvas.bind("<ButtonRelease-1>",self.reset)
        self.oldx=None
        self.oldy=None
        
    def draw(self, event):
        self.size=self.thicky.get()
        if self.eraser_on==True:
            pencolor="white"

        else:
            pencolor=self.color

        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=pencolor, width=self.size, smooth=True, splinesteps=36)

        self.oldx=event.x
        self.oldy=event.y

    def reset(self, event):
        self.oldx=None
        self.oldy=None

    def pen(self):
        self.eraser_on=False
    def eraser(self):
        self.eraser_on=True

    def color(self):
        self.color=askcolor()[1]
    def brush(self):
        self.eraser_on=False
paint=Paint()