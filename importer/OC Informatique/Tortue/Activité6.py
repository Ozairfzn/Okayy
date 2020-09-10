from turtle import *


tort1 = Turtle()
tort2 = Turtle()
tort3 = Turtle()
tort4 = Turtle()

tort1.speed("fastest")
tort2.speed("fastest")
tort3.speed("fastest")
tort4.speed("fastest")


tort1.color("red")
tort2.color("blue")
tort3.color("orange")
tort4.color("green")

tort1.penup()
tort2.penup()
tort3.penup()
tort4.penup()
tort1.goto(-200, -200)
tort2.goto(200, -200)
tort3.goto(200, 200)
tort4.goto(-200, 200)
tort1.pendown()
tort2.pendown()
tort3.pendown()
tort4.pendown()

for i in range(42):
    position1 = tort1.position()
    position2 = tort2.position()
    position3 = tort3.position()
    position4 = tort4.position()

    angle1 = tort1.towards(position2)
    tort1.setheading(angle1)
    angle2 = tort2.towards(position3)
    tort2.setheading(angle2)
    angle3 = tort3.towards(position4)
    tort3.setheading(angle3)
    angle4 = tort4.towards(position1)
    tort4.setheading(angle4)

    tort1.goto(position2)
    tort1.goto(position1)
    tort2.goto(position3)
    tort2.goto(position2)
    tort3.goto(position4)
    tort3.goto(position3)
    tort4.goto(position1)
    tort4.goto(position4)

    tort1.forward(10)
    tort2.forward(10)
    tort3.forward(10)
    tort4.forward(10)

exitonclick()
