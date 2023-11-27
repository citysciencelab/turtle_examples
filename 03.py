import turtle

# set the color of the line to "red" (1st parameter) and the fill to "yellow" (2nd parameter)
turtle.color('red', 'yellow')

# tell the turtle to fill the shape that it draws
turtle.begin_fill()

# create a loop that just keeps running ("True") no matter what (unless actively ended with "break")
while True:
    # go 200px forward and then turn left 110°
    turtle.forward(200)
    turtle.left(110)

    # when the turtle's position is smaller than 1px in any direction (meaning when it is back where it started)
    # break the loop
    if abs(turtle.pos()) < 1:
        break

# end the fill and apply the color
turtle.end_fill()
turtle.done()
