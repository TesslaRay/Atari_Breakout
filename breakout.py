# Atari Breakout in Python 3
# By @Cristian Valdivia

import turtle

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

# Structure
blue = turtle.Turtle()
blue.speed(0)
blue.shape("square")
blue.color("blue")
blue.shapesize(stretch_wid=1, stretch_len=5)
blue.penup()
blue.goto(0, 50)

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

    # Ball and structure collisions
    if (ball.ycor() > 40 and ball.ycor() < 50) and (ball.xcor() < blue.xcor() +  50 and ball.xcor() > blue.xcor() - 50) and blue.isvisible():
        ball.dy *= -1
        blue.hideturtle()
        score += 1
        pen.clear()
        pen.write("Points: {}".format(score), align="center", font=("Courier", 24,"normal"))