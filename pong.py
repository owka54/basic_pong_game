import turtle
import winsound

# Window setup
window = turtle.Screen()
window.title("Pong by Owen Kane")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))


# Functions
def paddle_up(paddle):
    if (paddle == 1):
        y = paddle_a.ycor()
        y += 20
        if (y > 240):
            paddle_a.sety(240)
        else:
            paddle_a.sety(y)
    else:
        y = paddle_b.ycor()
        y += 20
        if (y > 240):
            paddle_b.sety(240)
        else:
            paddle_b.sety(y)

def paddle_down(paddle):
    if (paddle == 1):
        y = paddle_a.ycor()
        y -= 20
        if (y < -240):
            paddle_a.sety(-240)
        else:
            paddle_a.sety(y)
    else:
        y = paddle_b.ycor()
        y -= 20
        if (y < -240):
            paddle_b.sety(-240)
        else:
            paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(lambda n=1: paddle_up(n), "w")
window.onkeypress(lambda n=1: paddle_down(n), "s")
window.onkeypress(lambda n=2: paddle_up(n), "Up")
window.onkeypress(lambda n=2: paddle_down(n), "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # Increase ball speed after collision with side
        ball.dy *= 1.03

    if (ball.ycor() < -285):
        ball.sety(-285)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= 1.03

    if (ball.xcor() > 390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        # Reset ball speed
        ball.dx = -0.3
        ball.dy = -0.3

    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        ball.dx = 0.3
        ball.dy = 0.3
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        # Increase ball speed after collision with paddle
        ball.dx *= 1.03

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= 1.03
