from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(3)
timmy.hideturtle()
timmy.penup()
timmy.goto(x=-125, y=-125)
screen = Screen()
screen.setup(500, 500)
screen.colormode(255)
color_list = [(238, 246, 244), (249, 243, 247), (1, 12, 31), (54, 25, 17),
              (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39), (216, 86, 63), (156, 6, 24),
              (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20), (175, 134, 162),
              (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85), (144, 227, 217), (121, 193, 147),
              (220, 177, 216), (100, 218, 229), (251, 198, 1), (116, 170, 192)]


def draw_dots():
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(15)
        timmy.penup()
        timmy.forward(30)


def turn_left():
    timmy.left(90)
    timmy.penup()
    timmy.forward(30)
    timmy.left(90)
    timmy.forward(30)


def turn_right():
    timmy.right(90)
    timmy.penup()
    timmy.forward(30)
    timmy.right(90)
    timmy.forward(30)


for _ in range(5):
    draw_dots()
    turn_left()
    draw_dots()
    turn_right()

screen.exitonclick()