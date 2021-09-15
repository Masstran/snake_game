from turtle import Turtle
TURTLE_SIZE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.setx(-TURTLE_SIZE * i)
            self.snake_body.append(turtle)

    def move(self):
        for block_id in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[block_id].setpos(self.snake_body[block_id - 1].pos())
        self.snake_body[0].forward(20)
