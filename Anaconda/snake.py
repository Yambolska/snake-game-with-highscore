from turtle import Turtle
starting_position = [0, -20, -40]
class Snake:
    def __init__(self,):
        self.pieces=[]
        self.create_snake()


    def zero(self):
        for i in self.pieces:
            i.teleport(1000,1000)
        self.pieces.clear()
        self.create_snake()



    def create_snake(self):
        for i in starting_position:
            new_pieces = Turtle(shape='square')
            new_pieces.color('white')
            new_pieces.penup()
            new_pieces.setx(i)
            self.pieces.append(new_pieces)

    def extend(self):
        new_pieces=Turtle(shape='square')
        new_pieces.color('white')
        new_pieces.penup()
        new_pieces.goto(self.pieces[-1].position())
        self.pieces.append(new_pieces)

    def right(self):
        if  self.pieces[0].heading()!=180:
            self.pieces[0].setheading(0)

    def left(self):
        if  self.pieces[0].heading()!=0:
            self.pieces[0].setheading(180)

    def up(self):
        if  self.pieces[0].heading()!=270:
            self.pieces[0].setheading(90)

    def down(self):
        if  self.pieces[0].heading()!=90:
            self.pieces[0].setheading(270)



    def move(self,):
        for i in range(len(self.pieces) - 1, 0, -1):
            new_x = self.pieces[i - 1].xcor()
            new_y = self.pieces[i - 1].ycor()
            self.pieces[i].goto(new_x, new_y)
        self.pieces[0].forward(20)