import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create a turtle object
galaxy = turtle.Turtle()
galaxy.speed(0)  # Set the fastest drawing speed

# Function to draw a star
def draw_star(x, y, size, color):
    galaxy.penup()
    galaxy.goto(x, y)
    galaxy.pendown()
    galaxy.color(color)
    galaxy.begin_fill()
    galaxy.circle(size)
    galaxy.end_fill()

# Function to generate random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw the galaxy
def draw_galaxy(num_stars):
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.uniform(0.1, 2.0)
        color = random_color()
        draw_star(x, y, size, color)

# Draw the galaxy
draw_galaxy(300)

# Hide the turtle and display the result
galaxy.hideturtle()
screen.mainloop()
