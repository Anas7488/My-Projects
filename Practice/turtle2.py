import turtle

turtle.pensize(3)

def draw_heart_curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        
turtle.color("red", "red")
turtle.bgcolor("lightgreen")
turtle.begin_fill()
turtle.speed(100)
turtle.left(140)
turtle.forward(111.65)
draw_heart_curve()

turtle.left(120)
draw_heart_curve()
turtle.forward(111.65)

turtle.end_fill()

turtle.color('Black')
style = ('Comic Sans MS', 30, 'italic')
turtle.write('Love', font=style, align='center',)


turtle.hideturtle()
turtle.done()