from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.create_scoreboard()
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add_score()
        snake.upsize()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for body in snake.all_bodies[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
