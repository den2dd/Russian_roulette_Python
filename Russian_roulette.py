import turtle

turtle.circle(20)

answer = ''
while answer != 'N':
    answer = turtle.textinput("Нарисовать окружность", "Y/N")
    if answer == 'Y':
        turtle.circle(30)
    else:
        pass