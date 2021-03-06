from turtle import Turtle
from config import TURTLE_SIZE

FORWARD_MOVEMENT = 20
TURN_SLEEP_STEPS = TURTLE_SIZE // FORWARD_MOVEMENT

RIGHT_DIRECTION = 0
UP_DIRECTION = 90
LEFT_DIRECTION = 180
DOWN_DIRECTION = 270

VERTICAL_DIRECTION = [UP_DIRECTION, DOWN_DIRECTION]
HORIZONTAL_DIRECTION = [LEFT_DIRECTION, RIGHT_DIRECTION]


class Snake:

    def __init__(self):
        # This is so you couldn't turn twice in one screen refresh
        self.turn_sleep_steps = 0
        self.snake_body = []
        self._create_snake_()
        self.head = self.snake_body[0]
        self.turn_buffer = None

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.snake_body.append(turtle)

    def _create_snake_(self):
        for i in range(3):
            position = (-TURTLE_SIZE * i, 0)
            self.add_segment(position)

    def extend(self):
        """Add a new segment to snake"""
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for block_id in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[block_id].setpos(self.snake_body[block_id - 1].pos())
        self.head.forward(FORWARD_MOVEMENT)
        if self.turn_sleep_steps > 0:
            self.turn_sleep_steps -= 1
        if self.turn_sleep_steps == 0 and self.turn_buffer is not None:
            self.turn_buffer()
            self.turn_buffer = None

    def is_dead(self) -> bool:
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < TURTLE_SIZE / 2:
                return True
        return False

    def _direction_(self):
        return self.head.heading()

    def up(self):
        if self._direction_() in HORIZONTAL_DIRECTION:
            if self.turn_sleep_steps == 0:
                self.head.setheading(UP_DIRECTION)
                self.turn_sleep_steps = TURN_SLEEP_STEPS
            elif self.turn_buffer is None:
                self.turn_buffer = self.up

    def down(self):
        if self._direction_() in HORIZONTAL_DIRECTION:
            if self.turn_sleep_steps == 0:
                self.head.setheading(DOWN_DIRECTION)
                self.turn_sleep_steps = TURN_SLEEP_STEPS
            elif self.turn_buffer is None:
                self.turn_buffer = self.down

    def left(self):
        if self._direction_() in VERTICAL_DIRECTION:
            if self.turn_sleep_steps == 0:
                self.head.setheading(LEFT_DIRECTION)
                self.turn_sleep_steps = TURN_SLEEP_STEPS
            elif self.turn_buffer is None:
                self.turn_buffer = self.left

    def right(self):
        if self._direction_() in VERTICAL_DIRECTION:
            if self.turn_sleep_steps == 0:
                self.head.setheading(RIGHT_DIRECTION)
                self.turn_sleep_steps = TURN_SLEEP_STEPS
            elif self.turn_buffer is None:
                self.turn_buffer = self.right
