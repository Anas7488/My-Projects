import math 
from turtle import *
def calculateY(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)
def calculateX(k):
    return 15*math.sin(k)**3

speed(100)
bgcolor("black")

for i in range(1000):
    x= calculateX(i)*10
    y= calculateY(i)*10

    goto(x,y)
    color('#f73487')
    goto(x,y)
color("white")
style = ('Comic Sans MS', 30, 'italic')
write('Love', font=style,align='center',)
done()
