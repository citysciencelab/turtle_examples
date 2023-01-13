import turtle
turtle.speed('fastest')
  
# turning the turtle to face upwards
turtle.right(-90)
  
# the acute angle between
# the base and branch of the Y
angle = 30
  
# function to plot a Y
def y(size, level):   
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
  
        # recursive call for
        # the right subtree
        y(0.8 * size, level-1)
          
        turtle.pencolor(0, 255//level, 0)
        turtle.left( 2 * angle )
  
        # recursive call for
        # the left subtree
        y(0.8 * size, level-1)
          
        turtle.pencolor(0, 255//level, 0)
        turtle.right(angle)
        turtle.forward(-size)
           
          
# tree of size 80 and level 7
y(80, 10)
turtle.done()