import turtle
import random

# Create a new turtle and store it to a variable, i.e. give it the name "hans" by which it can be called later
hans = turtle.Turtle()

# Set the shape of our turtle to be a "turtle" (This is a function built into the turtle library)
hans.shape("turtle")

# Create a variable that stores whether Hans has returned to his origin and set it to initially be false
hans_returned_home = False

# Create a loop that keeps running as long Hans is not back home
while not hans_returned_home:
    # Let Hans walk forward for 100px
    hans.forward(100)
    
    # if Hans is further away that 200px from home (the origin of his journey at the coordinates (0,0))
    # let him turn left or right randomly with a 50% chance
    # choosing the angle of the turn to be random between 0 and 180 degrees
    if turtle.distance((hans.pos()[0], hans.pos()[1]), (0,0)) > 200:
        if random.random() >= 0.5:
            hans.left(random.random() * 180)
        else:
            hans.right(random.random() * 180)
    # if Hans happens to get as close to home as 10px distance we end the loop by setting hans_returned_home to be true
    if turtle.distance((hans.pos()[0], hans.pos()[1]), (0,0)) < 10:
        hans_returned_home = True

turtle.done()
