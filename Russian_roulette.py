import turtle
import random
import math

PHI = 360 / 7
R = 50

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

turtle.speed(0)

def draw_pistol():
    gotoxy(0,0)
    turtle.circle(80)
    gotoxy(0,160)
    draw_circle(5, 'red')

    for i in range(0,7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad)*R, math.cos(phi_rad)*R + 60)
        draw_circle(22, 'white')

draw_pistol()

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Играть", "Y/N")
    if answer == 'Y':

        for i in range(start, random.randrange(7, 100)):
            phi_rad = PHI * i * math.pi / 180.0
            gotoxy(math.sin(phi_rad) * R, math.cos(phi_rad) * R + 60)
            draw_circle(22, 'brown')
            draw_circle(22, 'white')

        gotoxy(math.sin(phi_rad) * R, math.cos(phi_rad) * R + 60)
        draw_circle(22, 'brown')

        start = i % 7
        if start == 0:
            gotoxy(-150, 200)
            turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))

    else:
        pass