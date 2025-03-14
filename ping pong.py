import tkinter

screen=tkinter.Tk()
screen.geometry("800x600")
screen.title("PING PONG")

canvas=tkinter.Canvas(screen, width=800, height=600, bg="black")
canvas.grid(row=1,column=1)

canvas.create_line(400,0,400,800,fill="white",width=5)
circle=canvas.create_oval(400,400,600,600,outline="white",width=5)
canvas.move(circle,-95,-180)

class Ball():
    def __init__(self):
        self.ball=canvas.create_oval(10,10,30,30,fill="white")
        self.changex=5
        self.changey=5
        self.score1=0
        self.score2=0
    
    def draw(self):
        canvas.move(self.ball,self.changex,self.changey)


ball=Ball()

while True:
    ball.draw()
    screen.update_idletasks()
    screen.update()
screen.mainloop()