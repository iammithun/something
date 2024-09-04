# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:01:57 2024

@author: iamrs
"""

import turtle

house = turtle.Turtle()
house.speed(0) 


def draw_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)


def draw_triangle(turtle, size):
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)


def draw_house(turtle, size):

    turtle.color("blue")
    turtle.begin_fill()
    draw_square(turtle, size)
    turtle.end_fill()


    turtle.penup()
    turtle.goto(-size/2, 0)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    draw_triangle(turtle, size)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-size/4, -size/2)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    draw_square(turtle, size/2)
    turtle.end_fill()


house.penup()
house.goto(-100, -100)
house.pendown()

draw_house(house, 200)


house.hideturtle()
turtle.done()
