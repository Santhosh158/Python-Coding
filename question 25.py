
'''
25(Turtle: draw a rectangle) Write a program that prompts the user to enter the
center of a rectangle, width, and height, and displays the rectangle, as shown in
Figure 2.4c.
'''

import math, turtle
x1,y1,width,height = eval(input("Enter the center of rectangle, width and height"))

l = abs(x1) - width
w = abs(y1) - height

if l == 0:
    l = width // 2
elif w == 0:
    w = height // 2

l = abs(l)
w = abs(w)
turtle.showturtle()
turtle.penup()
turtle.goto(x1,y1)
turtle.forward(l)
turtle.pendown()
turtle.setheading(-90)
turtle.forward(w)
turtle.setheading(180)
turtle.forward(2 * l)
turtle.setheading(90)
turtle.forward(2 * w)
turtle.setheading(0)
turtle.forward(2 * l)
turtle.setheading(-90)
turtle.forward(w)
turtle.done()




