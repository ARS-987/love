import turtle
import time
for i in range (0,10):
    n = turtle.Turtle()
    n.color('red')
    n.begin_fill()
    n.fillcolor('red')
    n.left(140)
    n.forward(180)
    n.circle(-90, 200)
    n.setheading(60)
    n.circle(-90, 200)
    n.forward(180)
    n.end_fill()
    n.write('hi')
    time.sleep(.5)
    n.reset()