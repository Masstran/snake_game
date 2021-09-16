from turtle import Turtle
import random
from config import TURTLE_SIZE, HEIGHT, WIDTH


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.generate_random_location()

    def generate_random_location(self):
        screen = self.getscreen()
        screen_width = WIDTH
        screen_height = HEIGHT
        # 20 = size of normal turtle
        x_pace_to = screen_width // 2 // TURTLE_SIZE - 2
        y_pace_to = screen_height // 2 // TURTLE_SIZE - 2

        keep_going = True
        x_pos = 0
        y_pos = 0
        # Make sure that food doesn't spawn on the snake itself
        while keep_going:
            x_pos = random.randint(-x_pace_to, x_pace_to) * TURTLE_SIZE
            y_pos = random.randint(-y_pace_to, y_pace_to) * TURTLE_SIZE
            keep_going = False
            for turtle in screen.turtles():
                if turtle.shape() == "square" and turtle.xcor() == x_pos and turtle.ycor() == y_pos:
                    keep_going = True
                    break

        self.goto(x_pos, y_pos)
