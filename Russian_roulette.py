import turtle
import random

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.speed(0)

gotoxy(0,0)
turtle.circle(80)
gotoxy(0,160)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

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