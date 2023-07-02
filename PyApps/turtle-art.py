import random
import turtle

# Set the canvas size
turtle.screensize(800, 800)

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(0)

# Set the turtle's color
t.color("black")

# Set the turtle's line width
t.width(5)

# Start the loop
for i in range(500):

    # Generate a random number between 0 and 360
    angle = random.randint(0, 360)

    # Move the turtle forward by a random distance
    t.forward(random.randint(1, 100))

    # Turn the turtle left by the random angle
    t.left(angle)

# Hide the turtle
t.hideturtle()