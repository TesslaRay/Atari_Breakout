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
paddle.shapesize(stretch_wid=1, stretch_len=7)
paddle.penup()
paddle.goto(0 , -260) 

# Ball 
ball_move = 2
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0,0)
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

# # Functions
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
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
    if ball.ycor() > 290:
        ball.sety(290)
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
