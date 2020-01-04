# Atari Breakout in Python 3
# By @Cristian Valdivia

import turtle
from block import *

wn = turtle.Screen()
wn.title("Atari Breakout by @CristianValdivia")
wn.bgcolor("black")
wn.setup(width=1030, height=600)
wn.tracer(0)

# Paddle 
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0 , -260) 

# Ball 
ball_move = 5
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,-240)
ball.dx = ball_move
ball.dy = ball_move

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Points: 0", align="center", font=("Courier", 24,"normal"))

# Score
score = 0

# Functions
def paddle_right():
    x = paddle.xcor()
    x += 40
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 40
    paddle.setx(x)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")
 
# Main loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 270:
        ball.sety(270)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ball.goto(0, -240)

        blue0.showturtle()
        blue1.showturtle()
        blueM1.showturtle()
        blue2.showturtle()
        blueM2.showturtle()
        blue3.showturtle()
        blueM3.showturtle()
        blue4.showturtle()
        blueM4.showturtle()

        green0.showturtle()
        green1.showturtle()
        greenM1.showturtle()
        green2.showturtle()
        greenM2.showturtle()
        green3.showturtle()
        greenM3.showturtle()
        green4.showturtle()
        greenM4.showturtle()

        yellow0.showturtle()
        yellow1.showturtle()
        yellowM1.showturtle()
        yellow2.showturtle()
        yellowM2.showturtle()
        yellow3.showturtle()
        yellowM3.showturtle()
        yellow4.showturtle()
        yellowM4.showturtle()

        orange0.showturtle()
        orange1.showturtle()
        orangeM1.showturtle()
        orange2.showturtle()
        orangeM2.showturtle()
        orange3.showturtle()
        orangeM3.showturtle()
        orange4.showturtle()
        orangeM4.showturtle()

        red0.showturtle()
        red1.showturtle()
        redM1.showturtle()
        red2.showturtle()
        redM2.showturtle()
        red3.showturtle()
        redM3.showturtle()
        red4.showturtle()
        redM4.showturtle()

        score = 0
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if ball.xcor() > 490:
        ball.setx(490)
        ball.dx *= -1
     
    if ball.xcor() < -490:
        ball.setx(-490)
        ball.dx *= -1
    
    # Paddle and ball collisions
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 55 and ball.xcor() > paddle.xcor() - 55):
        ball.sety(-240)
        ball.dy *= -1

    # Ball and block collisions
    # Blue row
    if (ball.ycor() > blue0.ycor() - 20 and ball.ycor() < blue1.ycor() + 20) and (ball.xcor() < blue0.xcor() +  50 and ball.xcor() > blue0.xcor() - 50) and blue0.isvisible():
        ball.dy *= -1
        blue0.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > blue1.ycor() - 20 and ball.ycor() < blue1.ycor() + 20) and (ball.xcor() < blue1.xcor() +  50 and ball.xcor() > blue1.xcor() - 50) and blue1.isvisible():
        ball.dy *= -1
        blue1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > blueM1.ycor() - 20 and ball.ycor() < blueM1.ycor() + 20) and (ball.xcor() < blueM1.xcor() +  50 and ball.xcor() > blueM1.xcor() - 50) and blueM1.isvisible():
        ball.dy *= -1
        blueM1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > blue2.ycor() - 20 and ball.ycor() < blue2.ycor() + 20) and (ball.xcor() < blue2.xcor() +  50 and ball.xcor() > blue2.xcor() - 50) and blue2.isvisible():
        ball.dy *= -1
        blue2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    if (ball.ycor() > blueM2.ycor() - 20 and ball.ycor() < blueM2.ycor() + 20) and (ball.xcor() < blueM2.xcor() +  50 and ball.xcor() > blueM2.xcor() - 50) and blueM2.isvisible():
        ball.dy *= -1
        blueM2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))   
    
    if (ball.ycor() > blue3.ycor() - 20 and ball.ycor() < blue3.ycor() + 20) and (ball.xcor() < blue3.xcor() +  50 and ball.xcor() > blue3.xcor() - 50) and blue3.isvisible():
        ball.dy *= -1
        blue3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > blueM3.ycor() - 20 and ball.ycor() < blueM3.ycor() + 20) and (ball.xcor() < blueM3.xcor() +  50 and ball.xcor() > blueM3.xcor() - 50) and blueM3.isvisible():
        ball.dy *= -1
        blueM3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > blue4.ycor() - 20 and ball.ycor() < blue4.ycor() + 20) and (ball.xcor() < blue4.xcor() +  50 and ball.xcor() > blue4.xcor() - 50) and blue4.isvisible():
        ball.dy *= -1
        blue4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > blueM4.ycor() - 20 and ball.ycor() < blueM4.ycor() + 20) and (ball.xcor() < blueM4.xcor() +  50 and ball.xcor() > blueM4.xcor() - 50) and blueM4.isvisible():
        ball.dy *= -1
        blueM4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    # Green row
    if (ball.ycor() > green0.ycor() - 20 and ball.ycor() < green0.ycor() + 20) and (ball.xcor() < green0.xcor() +  50 and ball.xcor() > green0.xcor() - 50) and green0.isvisible():
        ball.dy *= -1
        green0.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > green1.ycor() - 20 and ball.ycor() < green1.ycor() + 20) and (ball.xcor() < green1.xcor() +  50 and ball.xcor() > green1.xcor() - 50) and green1.isvisible():
        ball.dy *= -1
        green1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > greenM1.ycor() - 20 and ball.ycor() < greenM1.ycor() + 20) and (ball.xcor() < greenM1.xcor() +  50 and ball.xcor() > greenM1.xcor() - 50) and greenM1.isvisible():
        ball.dy *= -1
        greenM1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > green2.ycor() - 20 and ball.ycor() < green2.ycor() + 20) and (ball.xcor() < green2.xcor() +  50 and ball.xcor() > green2.xcor() - 50) and green2.isvisible():
        ball.dy *= -1
        green2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    if (ball.ycor() > greenM2.ycor() - 20 and ball.ycor() < greenM2.ycor() +20) and (ball.xcor() < greenM2.xcor() +  50 and ball.xcor() > greenM2.xcor() - 50) and greenM2.isvisible():
        ball.dy *= -1
        greenM2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))   
    
    if (ball.ycor() > green3.ycor() - 20 and ball.ycor() < green3.ycor() + 20) and (ball.xcor() < green3.xcor() +  50 and ball.xcor() > green3.xcor() - 50) and green3.isvisible():
        ball.dy *= -1
        green3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > greenM3.ycor() - 20 and ball.ycor() < greenM3.ycor() + 20) and (ball.xcor() < greenM3.xcor() +  50 and ball.xcor() > greenM3.xcor() - 50) and greenM3.isvisible():
        ball.dy *= -1
        greenM3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > green4.ycor() - 20 and ball.ycor() < green4.ycor() + 20) and (ball.xcor() < green4.xcor() +  50 and ball.xcor() > green4.xcor() - 50) and green4.isvisible():
        ball.dy *= -1
        green4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > greenM4.ycor() - 20 and ball.ycor() < greenM4.ycor() + 20) and (ball.xcor() < greenM4.xcor() +  50 and ball.xcor() > greenM4.xcor() - 50) and greenM4.isvisible():
        ball.dy *= -1
        greenM4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    # Yellow row
    if (ball.ycor() > yellow0.ycor() - 20 and ball.ycor() < yellow0.ycor() + 20) and (ball.xcor() < yellow0.xcor() +  50 and ball.xcor() > yellow0.xcor() - 50) and yellow0.isvisible():
        ball.dy *= -1
        yellow0.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > yellow1.ycor() - 20 and ball.ycor() < yellow1.ycor() + 20) and (ball.xcor() < yellow1.xcor() +  50 and ball.xcor() > yellow1.xcor() - 50) and yellow1.isvisible():
        ball.dy *= -1
        yellow1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > yellowM1.ycor() - 20 and ball.ycor() < yellowM1.ycor() + 20) and (ball.xcor() < yellowM1.xcor() +  50 and ball.xcor() > yellowM1.xcor() - 50) and yellowM1.isvisible():
        ball.dy *= -1
        yellowM1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > yellow2.ycor() - 20 and ball.ycor() < yellow2.ycor() + 20) and (ball.xcor() < yellow2.xcor() +  50 and ball.xcor() > yellow2.xcor() - 50) and yellow2.isvisible():
        ball.dy *= -1
        yellow2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    if (ball.ycor() > yellowM2.ycor() - 20 and ball.ycor() < yellowM2.ycor() +20) and (ball.xcor() < yellowM2.xcor() +  50 and ball.xcor() > yellowM2.xcor() - 50) and yellowM2.isvisible():
        ball.dy *= -1
        yellowM2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))   
    
    if (ball.ycor() > yellow3.ycor() - 20 and ball.ycor() < yellow3.ycor() + 20) and (ball.xcor() < yellow3.xcor() +  50 and ball.xcor() > yellow3.xcor() - 50) and yellow3.isvisible():
        ball.dy *= -1
        yellow3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > yellowM3.ycor() - 20 and ball.ycor() < yellowM3.ycor() + 20) and (ball.xcor() < yellowM3.xcor() +  50 and ball.xcor() > yellowM3.xcor() - 50) and yellowM3.isvisible():
        ball.dy *= -1
        yellowM3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > yellow4.ycor() - 20 and ball.ycor() < yellow4.ycor() + 20) and (ball.xcor() < yellow4.xcor() +  50 and ball.xcor() > yellow4.xcor() - 50) and yellow4.isvisible():
        ball.dy *= -1
        yellow4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > yellowM4.ycor() - 20 and ball.ycor() < yellowM4.ycor() + 20) and (ball.xcor() <  yellowM4.xcor() +  50 and ball.xcor() > yellowM4.xcor() - 50) and yellowM4.isvisible():
        ball.dy *= -1
        yellowM4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    # Orange row
    if (ball.ycor() > orange0.ycor() - 20 and ball.ycor() < orange0.ycor() + 20) and (ball.xcor() < orange0.xcor() +  50 and ball.xcor() > orange0.xcor() - 50) and orange0.isvisible():
        ball.dy *= -1
        orange0.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > orange1.ycor() - 20 and ball.ycor() < orange1.ycor() + 20) and (ball.xcor() < orange1.xcor() +  50 and ball.xcor() > orange1.xcor() - 50) and orange1.isvisible():
        ball.dy *= -1
        orange1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > orangeM1.ycor() - 20 and ball.ycor() < orangeM1.ycor() + 20) and (ball.xcor() < orangeM1.xcor() +  50 and ball.xcor() > orangeM1.xcor() - 50) and orangeM1.isvisible():
        ball.dy *= -1
        orangeM1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > orange2.ycor() - 20 and ball.ycor() < orange2.ycor() + 20) and (ball.xcor() < orange2.xcor() +  50 and ball.xcor() > orange2.xcor() - 50) and orange2.isvisible():
        ball.dy *= -1
        orange2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    if (ball.ycor() > orangeM2.ycor() - 20 and ball.ycor() < orangeM2.ycor() +20) and (ball.xcor() < orangeM2.xcor() +  50 and ball.xcor() > orangeM2.xcor() - 50) and orangeM2.isvisible():
        ball.dy *= -1
        orangeM2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))   
    
    if (ball.ycor() > orange3.ycor() - 20 and ball.ycor() < orange3.ycor() + 20) and (ball.xcor() < orange3.xcor() +  50 and ball.xcor() > orange3.xcor() - 50) and orange3.isvisible():
        ball.dy *= -1
        orange3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > orangeM3.ycor() - 20 and ball.ycor() < orangeM3.ycor() + 20) and (ball.xcor() < orangeM3.xcor() +  50 and ball.xcor() > orangeM3.xcor() - 50) and orangeM3.isvisible():
        ball.dy *= -1
        orangeM3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > orange4.ycor() - 20 and ball.ycor() < orange4.ycor() + 20) and (ball.xcor() < orange4.xcor() +  50 and ball.xcor() > orange4.xcor() - 50) and orange4.isvisible():
        ball.dy *= -1
        orange4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > orangeM4.ycor() - 20 and ball.ycor() < orangeM4.ycor() + 20) and (ball.xcor() <  orangeM4.xcor() +  50 and ball.xcor() > orangeM4.xcor() - 50) and orangeM4.isvisible():
        ball.dy *= -1
        orangeM4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 
    
    # Red row
    if (ball.ycor() > red0.ycor() - 20 and ball.ycor() < red0.ycor() + 20) and (ball.xcor() < red0.xcor() +  50 and ball.xcor() > orange0.xcor() - 50) and red0.isvisible():
        ball.dy *= -1
        red0.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > red1.ycor() - 20 and ball.ycor() < red1.ycor() + 20) and (ball.xcor() < red1.xcor() +  50 and ball.xcor() > red1.xcor() - 50) and red1.isvisible():
        ball.dy *= -1
        red1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > redM1.ycor() - 20 and ball.ycor() < redM1.ycor() + 20) and (ball.xcor() < redM1.xcor() +  50 and ball.xcor() > redM1.xcor() - 50) and redM1.isvisible():
        ball.dy *= -1
        redM1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > red2.ycor() - 20 and ball.ycor() < red2.ycor() + 20) and (ball.xcor() < red2.xcor() +  50 and ball.xcor() > red2.xcor() - 50) and red2.isvisible():
        ball.dy *= -1
        red2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    if (ball.ycor() > redM2.ycor() - 20 and ball.ycor() < redM2.ycor() +20) and (ball.xcor() < redM2.xcor() +  50 and ball.xcor() > redM2.xcor() - 50) and redM2.isvisible():
        ball.dy *= -1
        redM2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))   
    
    if (ball.ycor() > red3.ycor() - 20 and ball.ycor() < red3.ycor() + 20) and (ball.xcor() < red3.xcor() +  50 and ball.xcor() > orange3.xcor() - 50) and red3.isvisible():
        ball.dy *= -1
        red3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > redM3.ycor() - 20 and ball.ycor() < redM3.ycor() + 20) and (ball.xcor() < redM3.xcor() +  50 and ball.xcor() > redM3.xcor() - 50) and redM3.isvisible():
        ball.dy *= -1
        redM3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > red4.ycor() - 20 and ball.ycor() < red4.ycor() + 20) and (ball.xcor() < red4.xcor() +  50 and ball.xcor() > orange4.xcor() - 50) and red4.isvisible():
        ball.dy *= -1
        red4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > redM4.ycor() - 20 and ball.ycor() < redM4.ycor() + 20) and (ball.xcor() <  redM4.xcor() +  50 and ball.xcor() > redM4.xcor() - 50) and redM4.isvisible():
        ball.dy *= -1
        redM4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 