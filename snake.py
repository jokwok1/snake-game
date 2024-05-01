from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #tuple for starting position
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  # create a 3 segment snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # add at position we are looping through

    # find a way to make the 2nd segment move to the 1st segment previous location, and 3rd to 2nd
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,
                             -1):  # input of start, stop, step, len func to ensure regards of length for loop occurs
            new_x = self.segments[seg_num - 1].xcor()  # get x cord of the body in front
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # move first bar by 20

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        """Add a new segment when food eaten"""
        self.add_segment(self.segments[-1].position()) # can get list of the last one of list using -1

    def up(self):
        if self.head.heading() != DOWN:  # prevents snake from going in opp direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # hide the previous snake
        self.segments.clear()  # remove all the snake body
        self.create_snake()
        self.head = self.segments[0]
