import turtle
turtle.speed('fastest')
  
# turning the turtle to face upwards
turtle.right(-90)
  
# the acute angle between
# the base and branch of the Y
angle = 30
  
# define a function to plot a Y
# that calls itself to draw a tree
# with a smaller Y being drawn on top of any Y until the end of the branches (level) is reached
def y(size, level):
    # draw a Y unless we reached level 0 (the outer most end of the tree)
    if level > 0:
        turtle.colormode(255)
          
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        turtle.pencolor(0, 255//level, 0)
          
        # drawing the base
        turtle.forward(size)
        turtle.right(angle)

        # once we reach the right top end of the Y
        # call the function itself again recursively
        # to the right subtree
        # this will happen until the the set number of levels has been drawn
        y(0.8 * size, level-1)
          
        turtle.pencolor(0, 255//level, 0)
        turtle.left( 2 * angle )
  
        # recursive call for
        # the left subtree
        # same as right
        y(0.8 * size, level-1)
          
        turtle.pencolor(0, 255//level, 0)
        turtle.right(angle)
        turtle.forward(-size)
           

# call the function to draw
# a tree of size 80 and level 10
y(80, 10)
turtle.done()
