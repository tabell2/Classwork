import turtle


def draw_triangle(t, base, height):
    """Draw a triangle for tree section"""
    t.begin_fill()
    t.goto(t.xcor() - base / 2, t.ycor())
    t.goto(t.xcor() + base / 2, t.ycor() + height)
    t.goto(t.xcor() + base / 2, t.ycor() - height)
    t.end_fill()


def draw_christmas_tree():
    # Setup screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Christmas Tree")
    screen.bgcolor("white")

    # Create turtle
    t = turtle.Turtle()
    t.speed(2)
    t.color("green")

    # Draw three triangle sections for the tree
    t.penup()
    t.goto(0, -200)
    t.pendown()

    # Bottom section (largest)
    draw_triangle(t, 200, 100)

    # Middle section
    t.penup()
    t.goto(0, -120)
    t.pendown()
    draw_triangle(t, 160, 90)

    # Top section (smallest)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    draw_triangle(t, 120, 80)

    # Draw trunk
    t.color("brown")
    t.penup()
    t.goto(-20, -200)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

    # Hide turtle
    t.hideturtle()

    # Keep window open
    screen.mainloop()


if __name__ == "__main__":
    draw_christmas_tree()