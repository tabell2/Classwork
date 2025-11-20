import turtle
import time
from datetime import datetime


def decimal_to_roman(num):
    """Convert a decimal number (1-59) to Roman numerals"""
    if num == 0:
        return "N"  # N for "nulla" (zero in Latin)

    val = [
        50, 40, 10, 9, 5, 4, 1
    ]
    syms = [
        'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num


def draw_letter(t, letter, size=40):
    """Draw a single Roman numeral letter using turtle graphics"""
    t.pendown()

    if letter == 'I':
        # Draw vertical line
        t.setheading(90)
        t.forward(size)
        t.backward(size)

    elif letter == 'V':
        # Draw V shape
        t.setheading(60)
        t.forward(size * 0.6)
        t.setheading(-60)
        t.forward(size * 0.6)
        t.backward(size * 0.6)
        t.setheading(60)
        t.backward(size * 0.6)

    elif letter == 'X':
        # Draw X shape
        t.setheading(60)
        t.forward(size * 0.8)
        t.backward(size * 0.8)
        t.setheading(-60)
        t.forward(size * 0.8)
        t.backward(size * 0.8)

    elif letter == 'L':
        # Draw L shape
        t.setheading(90)
        t.forward(size)
        t.backward(size)
        t.setheading(0)
        t.forward(size * 0.6)
        t.backward(size * 0.6)

    elif letter == 'N':
        # Draw N for zero (nulla)
        t.setheading(90)
        t.forward(size)
        t.setheading(-60)
        t.forward(size * 1.2)
        t.setheading(90)
        t.forward(size)
        t.backward(size)
        t.setheading(60)
        t.backward(size * 1.2)

    t.penup()


def draw_roman_numeral(t, roman_str, x, y, size=40):
    """Draw a complete Roman numeral string"""
    t.penup()
    t.goto(x, y)
    spacing = size * 0.5

    for letter in roman_str:
        draw_letter(t, letter, size)
        t.forward(spacing)


def parse_time_input(time_str):
    """Parse time input in various formats and return hours and minutes"""
    time_str = time_str.strip().upper()

    try:
        # Try to parse as 24-hour format (HH:MM)
        if ':' in time_str and ('AM' not in time_str and 'PM' not in time_str):
            hours, minutes = map(int, time_str.split(':'))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes

        # Try to parse as 12-hour format with AM/PM
        elif 'AM' in time_str or 'PM' in time_str:
            is_pm = 'PM' in time_str
            time_str = time_str.replace('AM', '').replace('PM', '').strip()

            if ':' in time_str:
                hours, minutes = map(int, time_str.split(':'))
            else:
                hours = int(time_str)
                minutes = 0

            # Convert to 24-hour format
            if is_pm and hours != 12:
                hours += 12
            elif not is_pm and hours == 12:
                hours = 0

            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes

        # Try just a number (assume it's hours)
        else:
            hours = int(time_str)
            if 0 <= hours <= 23:
                return hours, 0

    except ValueError:
        pass

    return None, None


def main():
    # Setup screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Roman Numeral Clock")
    screen.bgcolor("white")

    # Create turtle
    t = turtle.Turtle()
    t.speed(5)
    t.pensize(3)
    t.color("darkblue")

    # Get user input
    screen.tracer(0)  # Turn off animation temporarily

    time_input = screen.textinput("Time Input",
                                  "Enter time (Examples: 3:45 PM, 15:30, 9 AM):")

    if time_input:
        hours, minutes = parse_time_input(time_input)

        if hours is not None and minutes is not None:
            # Convert to 12-hour format for display
            display_hours = hours % 12
            if display_hours == 0:
                display_hours = 12

            # Convert to Roman numerals
            roman_hours = decimal_to_roman(display_hours)
            roman_minutes = decimal_to_roman(minutes)

            # Draw title
            t.penup()
            t.goto(-150, 200)
            t.color("black")
            title_writer = turtle.Turtle()
            title_writer.hideturtle()
            title_writer.penup()
            title_writer.goto(0, 220)
            title_writer.write("Roman Numeral Clock", align="center",
                               font=("Arial", 24, "bold"))

            # Display original time
            title_writer.goto(0, 180)
            am_pm = "AM" if hours < 12 else "PM"
            display_12hr = f"{display_hours}:{minutes:02d} {am_pm}"
            title_writer.write(f"Time: {display_12hr} ({hours:02d}:{minutes:02d})",
                               align="center", font=("Arial", 16, "normal"))

            screen.tracer(1)  # Turn animation back on

            # Draw hours label
            t.penup()
            t.goto(-200, 50)
            t.color("darkgreen")
            t.write("HOURS:", font=("Arial", 20, "bold"))

            # Draw hours in Roman numerals
            t.color("darkblue")
            draw_roman_numeral(t, roman_hours, -200, 0, size=50)

            # Draw minutes label
            t.penup()
            t.goto(-200, -80)
            t.color("darkgreen")
            t.write("MINUTES:", font=("Arial", 20, "bold"))

            # Draw minutes in Roman numerals
            t.color("darkred")
            draw_roman_numeral(t, roman_minutes, -200, -130, size=50)

            # Hide turtle
            t.hideturtle()

        else:
            error_turtle = turtle.Turtle()
            error_turtle.hideturtle()
            error_turtle.penup()
            error_turtle.goto(0, 0)
            error_turtle.color("red")
            error_turtle.write("Invalid time format!", align="center",
                               font=("Arial", 18, "bold"))

    screen.mainloop()


if __name__ == "__main__":
    main()