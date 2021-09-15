from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.onkey()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # for block_id, block in reversed(list(enumerate(snake))):
    #     if block_id == 0:
    #         block.forward(20)
    #     else:
    #         block.setpos(snake[block_id - 1].pos())

screen.exitonclick()
