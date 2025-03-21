import time
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
    def __init__(self): #self is actualy not as entitled as you think!
        self.ball=canvas.create_oval(10,10,30,30,fill="white")
        self.changex=5
        self.changey=5
        self.score1=0
        self.score2=0
    
    def draw(self):
        canvas.move(self.ball,self.changex,self.changey)
        self.position=canvas.coords(self.ball)
        if self.position[0]<=0:
            self.changex=5
            self.score2=self.score2+1

        if self.position[2]>=800:
            self.changex=-5
            self.score1=self.score1+1

        if self.position[1]<=0:
            self.changey=5

        if self.position[3]>=600:
            self.changey=-5

class Playerone():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(10,50,25,200,fill="Pink")
        self.changey=0
        canvas.bind_all('w',self.moveup)
        canvas.bind_all('s',self.movedown)

    def moveup(self, event): #yeah! get out of my way!
        self.changey=-5

    def movedown(self, event): #how do you even do that?
        self.changey=+5


    def draw(self):#live laugh love selfxdraw
         canvas.move(self.rectangle,0,self.changey)
         self.position=canvas.coords(self.rectangle)
         if self.position[1]<=0:
             self.changey=0

         if self.position[3]>=600:
             self.changey=0

class Playertwo():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(770,50,785,200,fill="Purple")
        self.changey=0
        canvas.bind_all('i',self.moveup)
        canvas.bind_all('k',self.movedown)

    def draw(self):#live laugh love self
         canvas.move(self.rectangle,0,self.changey)
         self.position=canvas.coords(self.rectangle)
         if self.position[1]<=0:
             self.changey=0

         if self.position[3]>=600:
             self.changey=0

    def moveup(self, event): #yeah! get out of my way!
        self.changey=-5

    def movedown(self, event): #how do you even do that?
        self.changey=+5


ball=Ball()
playerone=Playerone()
playertwo=Playertwo()


while True:
    ball.draw()
    playerone.draw()
    playertwo.draw()
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)
