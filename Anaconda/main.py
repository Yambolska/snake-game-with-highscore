from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
scoreboard=ScoreBoard()
screen=Screen()
screen.bgcolor('black')
screen.title('anaconda')
screen.setup(width=600,height=600)
screen.tracer(0)
starting_position=[0,-20,-40]
food=Food()
snake=Snake()
screen.listen()
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')


game=True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.pieces[0].distance(food)<15:
        food.replace()
        scoreboard.increase()
        snake.extend()

    if snake.pieces[0].xcor()>280 or snake.pieces[0].xcor()<-280 or snake.pieces[0].ycor()>280 or snake.pieces[0].ycor()<-280:
        scoreboard.high()
        snake.zero()

    for piece in snake.pieces[1:]:
        if snake.pieces[0].distance(piece) < 10:
            scoreboard.high()
            snake.zero()


