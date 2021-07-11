from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SHAPE = "square"
COLOR = "pink"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_bodies = []
        self.create_snake()
        self.head = self.all_bodies[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self, position):
        new_body = Turtle(SHAPE)
        new_body.color(COLOR)
        new_body.penup()
        new_body.goto(position)
        self.all_bodies.append(new_body)

    def upsize(self):
        self.add_body(self.all_bodies[-1].position())

    def move(self):
        for body_number in range(len(self.all_bodies) - 1, 0, -1):
            new_x = self.all_bodies[body_number - 1].xcor()
            new_y = self.all_bodies[body_number - 1].ycor()
            self.all_bodies[body_number].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for body in self.all_bodies:
            body.goto(1000, 1000)
        self.all_bodies.clear()
        self.create_snake()
        self.head = self.all_bodies[0]
