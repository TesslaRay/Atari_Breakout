# Atari Breakout in Python 3
# By @Cristian Valdivia

import turtle
from block import *

wn = turtle.Screen()
wn.title("Atari Breakout by @CristianValdivia")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0)

# Paddle 
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0 , -260) 

# Ball 
ball_move = 4
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
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
    x += 30
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 30
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
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1

    # Ball and block collisions
    # Blue row
    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blue0.xcor() +  50 and ball.xcor() > blue0.xcor() - 50) and blue0.isvisible():
        ball.dy *= -1
        blue0.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blue1.xcor() +  50 and ball.xcor() > blue1.xcor() - 50) and blue1.isvisible():
        ball.dy *= -1
        blue1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blueM1.xcor() +  50 and ball.xcor() > blueM1.xcor() - 50) and blueM1.isvisible():
        ball.dy *= -1
        blueM1.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blue2.xcor() +  50 and ball.xcor() > blue2.xcor() - 50) and blue2.isvisible():
        ball.dy *= -1
        blue2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal")) 

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blueM2.xcor() +  50 and ball.xcor() > blueM2.xcor() - 50) and blueM2.isvisible():
        ball.dy *= -1
        blueM2.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))   
    
    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blue3.xcor() +  50 and ball.xcor() > blue3.xcor() - 50) and blue3.isvisible():
        ball.dy *= -1
        blue3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blueM3.xcor() +  50 and ball.xcor() > blueM3.xcor() - 50) and blueM3.isvisible():
        ball.dy *= -1
        blueM3.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blue4.xcor() +  50 and ball.xcor() > blue4.xcor() - 50) and blue4.isvisible():
        ball.dy *= -1
        blue4.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))  

    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blueM4.xcor() +  50 and ball.xcor() > blueM4.xcor() - 50) and blueM4.isvisible():
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