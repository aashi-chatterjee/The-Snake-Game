from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    # to make the snake
    def create_snake(self):
        for position in STARTING_POS:
            self.add_tail(position)

    def add_tail(self, position):
        new_square = Turtle(shape="circle")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        new_square.speed("slow")
        self.full_snake.append(new_square)

    def extend(self):
        self.add_tail(self.full_snake[-1].position())

    # to move the snake
    def move(self):
        #                 range(start, stop, step)
        for snake_part in range(len(self.full_snake) - 1, 0, -1):
            second_last_x = self.full_snake[snake_part - 1].xcor()
            second_last_y = self.full_snake[snake_part - 1].ycor()
            self.full_snake[snake_part].goto(second_last_x, second_last_y)
        self.full_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
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
