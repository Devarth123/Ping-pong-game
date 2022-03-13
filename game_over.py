from turtle import Turtle


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("Game Over", font=("Courier", 120, "normal"), align="center")
