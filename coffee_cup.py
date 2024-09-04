import turtle

# Function to draw a filled circle
def draw_circle(t, color, radius):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(t, color, width, height):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Initialize turtle
cup = turtle.Turtle()
cup.speed(0)  # Set the speed to the fastest

# Draw the cup
cup.penup()
cup.goto(-50, -150)
cup.pendown()
draw_rectangle(cup, "brown", 100, 150)

# Draw the upper part of the cup
cup.penup()
cup.goto(-60, 0)
cup.pendown()
draw_circle(cup, "brown", 70)

# Draw the handle
cup.penup()
cup.goto(-10, 0)
cup.pendown()
cup.left(90)
draw_rectangle(cup, "brown", 20, 40)

# Hide turtle
cup.hideturtle()

# Keep the window open
turtle.done()
