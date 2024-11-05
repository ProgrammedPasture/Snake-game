from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Building the snake
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


#creating the snake
    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        amber = Turtle("square")
        amber.penup()
        amber.color("white")
        amber.goto(positions)
        self.segments.append(amber)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

#extending the snake when it scores a point
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


#Snake ability to move
    def move(self):
            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

#Giving the snake the ability to turn
    def turn_snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
