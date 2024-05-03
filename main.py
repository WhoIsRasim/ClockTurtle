import turtle
from datetime import datetime


screen = turtle.Screen()
screen.setup(500, 500, 0, 0)
screen.screensize(480, 480, bg="#ccc")
screen.tracer(0)

uzbek = turtle.Turtle()


def draw_lines(length, rotation):
    uzbek.penup()
    uzbek.home()
    uzbek.color("black")
    uzbek.pensize(1)
    uzbek.right(rotation)
    uzbek.forward(170)
    uzbek.pendown()
    uzbek.forward(length)
    uzbek.penup()



turtle.done()