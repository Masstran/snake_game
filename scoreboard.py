from turtle import Turtle
from config import HEIGHT, WIDTH

ALIGNMENT = 'center'
FONT = ("Courier", 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(0, HEIGHT // 2 - 30)
        self.score = 0
        self.refresh()

    def refresh(self):
        # self.pendown()
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        # self.penup()

    def add(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
