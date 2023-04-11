from turtle import Turtle, Screen

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle = []
        self.create_right_paddle()
        self.create_left_paddle()
        self.right_paddle = self.paddle[0]
        self.left_paddle = self.paddle[1]

    def create_right_paddle(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.penup()
        paddle.goto(400, 0)
        paddle.shapesize(5, 1)
        paddle.speed("fastest")
        self.paddle.append(paddle)

    def create_left_paddle(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.penup()
        paddle.goto(-400, 0)
        paddle.shapesize(5, 1)
        paddle.speed("fastest")
        self.paddle.append(paddle)

    def can_move(self):
        screen = Screen()
        screen.listen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkey(self.left_paddle_up, "w")
        screen.onkey(self.left_paddle_down, "s")

    def up(self):
        new_y = self.right_paddle.ycor() + 20
        self.right_paddle.goto(400, new_y)

    def down(self):
        new_y = self.right_paddle.ycor() - 20
        self.right_paddle.goto(400, new_y)

    def left_paddle_up(self):
        new_y = self.left_paddle.ycor() + 20
        self.left_paddle.goto(-400, new_y)

    def left_paddle_down(self):
        new_y = self.left_paddle.ycor() - 20
        self.left_paddle.goto(-400, new_y)
