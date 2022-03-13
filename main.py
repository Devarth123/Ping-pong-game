from score import Scoreboard
from r_paddle import R_paddle
from turtle import Screen, exitonclick
from ball import Ball
import time
from game_over import Game

game_is_on = True
number_of_cycles = int(input("How many times wud u like to play this game? :"))
screen = Screen()
score = Scoreboard()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.setup(width=1000, height=600)
l_paddle_in_game = R_paddle((-480, 0))
r_paddle_in_game = R_paddle((470, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle_in_game.go_up, "w")
screen.onkey(r_paddle_in_game.go_down, "s")
screen.onkey(l_paddle_in_game.go_up, "Up")
screen.onkey(l_paddle_in_game.go_down, "Down")
while game_is_on:
    if score.l_score == number_of_cycles or score.r_score == number_of_cycles:
        game_over = Game()
        game_is_on = False
    score.update_scoreboard()
    time.sleep(ball.move_sped)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncboucny_Y()
    if ball.distance(r_paddle_in_game) < 50 and ball.xcor() > 450 or ball.distance(
            l_paddle_in_game) < 50 and ball.xcor() < -450:
        ball.bouncboucny_X()
    if ball.xcor() > 500.0:
        score.sumscore_r()
        ball.reset()
    if ball.xcor() < -500.0:
        score.sumscore_l()
        ball.reset()

exitonclick()
