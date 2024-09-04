import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rotating Colorful Galaxy")

# Create a turtle for drawing the galaxy
galaxy_turtle = turtle.Turtle()
galaxy_turtle.speed(0)  # Fastest speed
galaxy_turtle.hideturtle()
galaxy_turtle.penup()

# Parameters for the galaxy
num_stars = 500  # Number of stars in the galaxy
angle_increment = 5  # Angle increment for the spiral arms
radius_increment = 0.5  # Radius increment for the spiral arms
rotation_speed = 0.1  # Rotation speed of the galaxy

# Function to draw a star
def draw_star(turtle, x, y, size, color):
    turtle.goto(x, y)
    turtle.color(color)
    turtle.dot(size)

# Generate stars in a spiral pattern
stars = []
for i in range(num_stars):
    angle = i * angle_increment
    radius = i * radius_increment
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    size = random.uniform(1, 3)
    color = (random.random(), random.random(), random.random())
    stars.append((x, y, size, color))

# Function to rotate the stars
def rotate_stars(stars, angle):
    rotated_stars = []
    for x, y, size, color in stars:
        new_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
        new_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
        rotated_stars.append((new_x, new_y, size, color))
    return rotated_stars

# Function to draw the galaxy
def draw_galaxy(turtle, stars):
    turtle.clear()
    for x, y, size, color in stars:
        draw_star(turtle, x, y, size, color)
    screen.update()

# Main loop to animate the galaxy
angle = 0
while True:
    rotated_stars = rotate_stars(stars, angle)
    draw_galaxy(galaxy_turtle, rotated_stars)
    angle += rotation_speed

# Keep the window open
turtle.done()
