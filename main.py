from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from config import HEIGHT, WIDTH
import time


def draw_border():
    border_drawer = Turtle()
    border_drawer.penup()
    border_drawer.speed("fastest")
    border_drawer.hideturtle()
    border_drawer.color("white")
    border_drawer.goto(-WIDTH // 2 + 10, -HEIGHT // 2 + 10)
    border_drawer.pendown()
    border_drawer.sety(HEIGHT // 2 - 10)
    border_drawer.setx(WIDTH // 2 - 10)
    border_drawer.sety(-HEIGHT // 2 + 10)
    border_drawer.setx(-WIDTH // 2 + 10)


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
draw_border()

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
        snake.extend()
        food.generate_random_location()

    # Detect collision with wall
    if abs(snake.head.xcor()) > WIDTH / 2 - 20 or abs(snake.head.ycor()) > HEIGHT / 2 - 20:
        game_is_on = False

    # Detect snake
    if snake.is_dead():
        game_is_on = False

snake.head.color("red")
screen.update()
score.game_over()
screen.exitonclick()
