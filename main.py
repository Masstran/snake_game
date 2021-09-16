from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from config import HEIGHT, WIDTH
import time


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.add()
        food.generate_random_location()

    # Detect collision with wall
    if abs(snake.head.xcor()) > WIDTH / 2 - 20 or abs(snake.head.ycor()) > HEIGHT / 2 - 20:
        game_is_on = False


score.game_over()
screen.exitonclick()
