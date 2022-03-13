from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_sped = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bouncboucny_Y(self):
        self.y_move *= -1

    def bouncboucny_X(self):
        self.x_move *= -1
        self.move_sped *= 0.9
    def reset(self):
        self.home()
        self.move_sped = 0.2
        self.bouncboucny_X()
