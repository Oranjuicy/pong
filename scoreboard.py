from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.draw_line()
        self.score_keeping()

    def draw_line(self):
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        while 301 > self.ycor() > -301:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def score_keeping(self):
        self.goto(0, 240)
        self.write(f"{self.score_left}  {self.score_right}", align="center", font=("Courier", 50, "normal"))

    def add_point(self, player):
        if player == "left":
            self.score_left += 1
        else:
            self.score_right += 1
        self.reset()
        self.draw_line()
        self.score_keeping()

    def winner(self):
        if self.score_left == 5:
            return "Player 1"
        else:
            return "Player 2"
