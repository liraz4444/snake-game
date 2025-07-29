import turtle
class Snake:
        START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        UP = 90
        DOWN = 270
        RIGHT = 0
        LEFT = 180

        def __init__(self):
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]

        def create_snake(self):
            for position in self.START_POSITIONS:
                self.add_segment(position)

        def add_segment(self,position):
            segment = turtle.Turtle()
            segment.shape("square")
            segment.color("blue")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

        def extend(self):
            self.add_segment(self.segments[-1].position())

        def move(self):
            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)

            self.segments[0].forward(20)

        def go_up(self):
            if self.segments[0].heading() != self.DOWN:
                self.segments[0].setheading(self.UP)

        def go_down(self):
            if self.segments[0].heading() != self.UP:
                self.segments[0].setheading(self.DOWN)

        def go_left(self):
            if self.segments[0].heading() != self.RIGHT:
                self.segments[0].setheading(self.LEFT)

        def go_right(self):
            if self.segments[0].heading() != self.LEFT:
                self.segments[0].setheading(self.RIGHT)




