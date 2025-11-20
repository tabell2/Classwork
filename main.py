import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("dark grey")
screen.title("Snowfall Simulation")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create a list to hold snowflakes
snowflakes = []

# Snowflake generator
def create_snowflake():
    flake = turtle.Turtle()
    flake.shape("circle")
    flake.color("white")
    flake.penup()
    flake.speed(0)
    flake.goto(random.randint(-380, 380), random.randint(250, 350))
    flake.shapesize(random.uniform(0.1, 0.3))  # random flake size
    flake.dy = random.uniform(1, 3)            # falling speed
    return flake

# Create initial snowflakes
for _ in range(300):
    snowflakes.append(create_snowflake())

# Animation loop
while True:
    for flake in snowflakes:
        flake.sety(flake.ycor() - flake.dy)

        # Respawn when off-screen
        if flake.ycor() < -300:
            flake.goto(random.randint(-380, 380), random.randint(250, 350))
            flake.dy = random.uniform(1, 3)

    screen.update()
    time.sleep(0.02)

# Keeps the window open (usually unreachable due to infinite loop)
turtle.done()