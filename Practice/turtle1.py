import turtle 
t = turtle.Turtle()
t.pensize(2)

x = t.getscreen()
x.bgcolor("Black")
t.speed(1999)
for i in range(400):
    t.forward(i+3)
    t.right(89)
    t.color("red")
t.done()