from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def create_snake():
    new_snake = []
    for i in range(3):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.setx(0 - 20 * i)
        new_snake.append(turtle)
    return new_snake


snake = create_snake()

game_is_on = True

count = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for block_id in range(len(snake) - 1, 0, -1):
        snake[block_id].setpos(snake[block_id - 1].pos())

    snake[0].forward(20)

    # for block_id, block in reversed(list(enumerate(snake))):
    #     if block_id == 0:
    #         block.forward(20)
    #     else:
    #         block.setpos(snake[block_id - 1].pos())
    if count % 10 == 0:
        snake[0].left(90)
    count += 1

screen.exitonclick()
