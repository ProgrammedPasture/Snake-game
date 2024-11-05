from pickle import FALSE
from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake-game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detection of snake getting the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.snake_scores()

    #Detection of snake colliding with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

    #Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()





screen.exitonclick()

