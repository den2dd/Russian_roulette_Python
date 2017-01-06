import turtle
import random

turtle.speed(0)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(80)

answer = ''
while answer != 'N':
    answer = turtle.textinput("Нарисовать окружность", "Y/N")
    if answer == 'Y':
        turtle.penup()
        turtle.goto(random.randrange(-300,300), random.randrange(-200,200))
        turtle.pendown()
        turtle.circle(random.randrange(1,100))
    else:
        pass