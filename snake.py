from turtle import Screen, Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    from turtle import Screen, Turtle
    def __init__(self):
        self.snake = []
        for x in range(0, 3):
            self.add_segment((-x * 20, 0))

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snake.append(new_seg)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[x - 1].xcor()
            new_y = self.snake[x - 1].ycor()
            self.snake[x].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)