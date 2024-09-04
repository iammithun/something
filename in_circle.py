# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:33:21 2024

@author: iamrs
"""
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Rainbow colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Drawing the infinity symbol
for i in range(100):
    t.pensize(2)
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.left(30)

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()

