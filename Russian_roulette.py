import turtle
import random

turtle.circle(20)

answer = ''
while answer != 'N':
    answer = turtle.textinput("Нарисовать окружность", "Y/N")
    if answer == 'Y':
        turtle.goto(random.randrange(-300,300), random.randrange(-200,200))
        turtle.circle(random.randrange(1,100))
    else:
        pass