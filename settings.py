import turtle

gravity = -0.005  # pixels/(time of iteration)^2
velocity = 0  # pixels/(time of iteration)
width = 600
height = 800
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)
ball = turtle.Turtle()
ball.penup()
ball.color("green")
ball.shape("circle")
while True:
    ball.sety(ball.ycor() + velocity)
    velocity += gravity
    if ball.ycor() < -height / 2:
        velocity = -velocity
    window.update()

