import turtle
import random

hans = turtle.Turtle()
hans.shape("turtle")

# hans.penup()
# hans.goto(-120, -150)
# hans.pendown()

while True:
    hans.forward(100)
    if turtle.distance((hans.pos()[0], hans.pos()[1]), (0,0)) > 200:
        # turtle.circle(50, 180)
        if random.random() >= 0.5:
            hans.left(random.random() * 120)
        else:
            hans.right(random.random() * 120)

turtle.done()