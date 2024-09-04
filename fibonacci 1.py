import turtle

def fibonacci_spiral(n):
    a, b = 0, 1
    t = turtle.Turtle()
    t.speed(1)

    for _ in range(n):
        t.forward(b * 10)  # Scale the length for visibility
        t.right(90)
        a, b = b, a + b

    turtle.done()

# Draw Fibonacci spiral for the first 10 Fibonacci numbers
fibonacci_spiral(10)
