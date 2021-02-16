'''1.18 (Turtle: draw a star) Write a program that draws a star, as shown in Figure 1.19c.
(Hint: The inner angle of each point in the star is 36 degrees.)
'''

import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.goto(100,-150)
turtle.goto(-160,30)
turtle.goto(160,30)
turtle.goto(-100,-150)
turtle.goto(0,150)
turtle.done()