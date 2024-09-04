# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:14:02 2024

@author: iamrs
"""

import turtle

def draw_body():
    # Head
    turtle.circle(40)
    
    # Body
    turtle.penup()
    turtle.goto(0, -40)
    turtle.pendown()
    turtle.forward(80)
    
    # Arms
    turtle.penup()
    turtle.goto(0, -40)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(60)
    turtle.backward(60)
    turtle.right(90)
    turtle.forward(60)
    
    # Legs
    turtle.penup()
    turtle.goto(0, -80)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(80)
    turtle.backward(80)
    turtle.right(90)
    turtle.forward(80)
    
def main():
    turtle.speed(1)
    draw_body()
    turtle.done()

if __name__ == "__main__":
    main()
