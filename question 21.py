
import time, turtle

ActaulTIme =  ("{0}:{1}:{2}".format(9,15,00))

turtle.speed(50)
turtle.penup()
turtle.goto(0,-193)
turtle.write(6)
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(200)
turtle.penup()
turtle.goto(0,180)
turtle.pendown()
turtle.write(12)
turtle.write(12)
turtle.penup()
turtle.goto(190,0)
turtle.pendown()
turtle.write(3)
turtle.penup()
turtle.goto(-190,0)
turtle.pendown()
turtle.write(9)


turtle.penup()
turtle.goto(0,0)
turtle.setheading(90)

turtle.pendown()
turtle.forward(130)
turtle.penup()
turtle.goto(-15,-220)
turtle.write(ActaulTIme)

turtle.penup()
turtle.goto(0,0)
turtle.setheading(0)

turtle.pendown()
turtle.forward(180)

turtle.penup()
turtle.goto(0,0)
turtle.setheading(180)

turtle.pendown()
turtle.forward(180)
turtle.hideturtle()
turtle.done()
