import turt
# we use a simplified version of the turtle interface
# written for use with SVGWrite

turtle = turt.SVGTurtle("koch.svg")
turtle.moveTo(100,500)

def koch(n,ln):
    if(n==0):
        turtle.forward(ln)
    else:
        koch(n-1,ln/3)
        turtle.turn(-60)
        koch(n-1,ln/3)
        turtle.turn(120)
        koch(n-1,ln/3)
        turtle.turn(-60)
        koch(n-1,ln/3)

koch(5,500)
turtle.end()
