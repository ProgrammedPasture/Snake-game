from turtle import Screen
import time
from snake import Snake

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake-game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.turn_snake_up,"Up")
screen.onkey(snake.turn_snake_down,"Down")
screen.onkey(snake.turn_snake_left,"Left")
screen.onkey(snake.turn_snake_right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()






screen.exitonclick()

