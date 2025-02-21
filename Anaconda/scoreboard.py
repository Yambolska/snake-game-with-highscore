from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,):
        super().__init__()
        self.penup()
        self.teleport(x=-20,y=270)
        self.color('white')
        self.hideturtle()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.highscore=int(file.read())
        self.write(arg=f'Score:{self.score} HighScore:{self.highscore} ',align='center',font=('Arial', 20, 'normal'))

    def game_over(self):
        self.home()
        self.write(arg=f'GAME OVER',align='center',font=('Arial', 20, 'normal'))

    def high(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.highscore}')
        self.clear()
        self.score=0
        self.write(arg=f'Score:{self.score} HighScore:{self.highscore} ',align='center',font=('Arial', 20, 'normal'))

    def increase(self):
        self.clear()
        self.score+=1
        self.write(arg=f'Score:{self.score} HighScore:{self.highscore} ',align='center',font=('Arial', 20, 'normal'))

