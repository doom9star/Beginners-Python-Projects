def square():
    myturtle.speed(10)
    myturtle.forward(100)
    myturtle.right(90)
    myturtle.forward(100)
    myturtle.right(90)
    myturtle.forward(100)
    myturtle.right(90)
    myturtle.forward(100)

import turtle as tl
myturtle = tl.Turtle()

for i in range(100):
    myturtle.color("green")
    square()
    myturtle.right(101)

