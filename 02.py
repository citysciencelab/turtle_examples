import turtle
import random

hans = turtle.Turtle()
hans.shape("turtle") 

def up():
    hans.setheading(90)
    hans.forward(100)

def down():
    hans.setheading(270)
    hans.forward(100)

def left():
    hans.setheading(180)
    hans.forward(100)

def right():
    hans.setheading(0)
    hans.forward(100)

colors = ["red", "blue", "green", "yellow", "black", "pink"]

def clickLeft(x, y):  # Make sure to have parameters x, y
    hans.color(random.choice(colors))

def clickRight(x, y):
    hans.stamp()

turtle.listen()

turtle.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRight, 3) # 3: Right Mouse Button

turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()  # This will make sure the program continues to run 