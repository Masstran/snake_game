from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


def create_snake():
    new_snake = []
    for i in range(3):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.setx(0 - 20 * i)
        new_snake.append(turtle)
    return new_snake


snake = create_snake()

screen.exitonclick()
