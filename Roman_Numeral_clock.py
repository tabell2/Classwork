import turtle

def digit_to_roman(digit):
    # Map digits to Roman numerals as they appear on a clock
    roman_map = {
        '0': '',
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX',
        '10': 'X',
        '11': 'XI',
        '12': 'XII'
    }
    return roman_map.get(str(digit), '')

def parse_time(time_str):
    time_str = time_str.strip().upper()

    # Check for AM/PM format
    if 'AM' in time_str or 'PM' in time_str:
        period = 'PM' if 'PM' in time_str else 'AM'
        time_str = time_str.replace('AM', '').replace('PM', '').strip()

        parts = time_str.split(':')
        if len(parts) != 2:
            raise ValueError("Invalid format")

        hours = int(parts[0])
        minutes = int(parts[1])

        if hours < 1 or hours > 12:
            raise ValueError("Hours must be 1-12 for AM/PM")

        # Convert to 24-hour
        if period == 'AM':
            if hours == 12:
                hours = 0
        else:  # PM
            if hours != 12:
                hours += 12
    else:
        # 24-hour format
        parts = time_str.split(':')
        if len(parts) != 2:
            raise ValueError("Invalid format")

        hours = int(parts[0])
        minutes = int(parts[1])

    # Validate
    if hours < 0 or hours > 23:
        raise ValueError("Hours must be 0-23")
    if minutes < 0 or minutes > 59:
        raise ValueError("Minutes must be 0-59")

    return hours, minutes


def draw_letter(t, letter, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)

    height = 60
    width = 30

    if letter == 'I':
        t.forward(height)

    elif letter == 'V':
        t.penup()
        t.goto(x, y + height)
        t.pendown()
        t.goto(x + width / 2, y)
        t.goto(x + width, y + height)

    elif letter == 'X':
        t.penup()
        t.goto(x, y + height)
        t.pendown()
        t.goto(x + width, y)
        t.penup()
        t.goto(x + width, y + height)
        t.pendown()
        t.goto(x, y)


def draw_roman_numeral(t, roman_str, start_x, y):
    spacing = 40
    x = start_x

    for char in roman_str:
        draw_letter(t, char, x, y)
        x += spacing


def draw_colon(t, x, y):
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.dot(12)
    t.penup()
    t.goto(x, y + 15)
    t.pendown()
    t.dot(12)


def draw_time(hours, minutes, screen, t):
    t.clear()

    # Convert time to string with leading zeros
    time_str = f"{hours:02d}:{minutes:02d}"

    # Convert hour digits - special handling for 10, 11, 12
    if hours == 10:
        hour_roman = 'X'
    elif hours == 11:
        hour_roman = 'XI'
    elif hours == 12:
        hour_roman = 'XII'
    else:
        digit1 = digit_to_roman(time_str[0])  # First hour digit
        digit2 = digit_to_roman(time_str[1])  # Second hour digit
        hour_roman = None

    # Convert minute digits
    digit3 = digit_to_roman(time_str[3])  # First minute digit
    digit4 = digit_to_roman(time_str[4])  # Second minute digit

    t.speed(1)
    t.pensize(3)
    t.color("black")

    # Calculate starting positions
    max_width = 40 * 4  # Maximum width for a digit
    gap = 10  # Gap between digits
    colon_space = 60

    # Starting x position
    if hour_roman:
        total_width = max_width * 3 + gap + colon_space
    else:
        total_width = max_width * 4 + gap * 2 + colon_space
    start_x = -total_width / 2

    y_pos = -30

    # Draw hour
    x_pos = start_x
    if hour_roman:
        # Draw as single numeral (X, XI, XII)
        draw_roman_numeral(t, hour_roman, x_pos, y_pos)
        x_pos += max_width + gap
    else:
        # Draw as two separate digits
        draw_roman_numeral(t, digit1, x_pos, y_pos)
        x_pos += max_width + gap
        draw_roman_numeral(t, digit2, x_pos, y_pos)
        x_pos += max_width + gap

    # Draw colon
    x_pos += colon_space / 2
    draw_colon(t, x_pos, y_pos)

    # Draw first minute digit
    x_pos += colon_space / 2 + gap
    draw_roman_numeral(t, digit3, x_pos, y_pos)

    # Draw second minute digit
    x_pos += max_width + gap
    draw_roman_numeral(t, digit4, x_pos, y_pos)

    # Hide turtle
    t.hideturtle()


def main():
    # Set up turtle screen
    screen = turtle.Screen()
    screen.setup(width=1000, height=500)
    screen.title("Roman Numeral Time")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()

    # Display instructions
    t.penup()
    t.goto(0, 100)
    t.write("Roman Numeral Time Converter", align="center", font=("Arial", 24, "bold"))
    t.goto(0, 60)
    t.write("Enter time below", align="center", font=("Arial", 16, "normal"))

    while True:
        try:
            # Get time input from user
            time_input = screen.textinput("Time Input", "Enter time:")

            if time_input is None:
                break

            hours, minutes = parse_time(time_input)

            # Draw the time
            draw_time(hours, minutes, screen, t)
            break

        except ValueError as e:
            # Show error message
            result = screen.textinput("Error", f"Invalid time format. Try again?\n(Enter 'yes' to continue)")
            if result is None or result.lower() != 'yes':
                break
        except Exception:
            break

    # Keep window open
    screen.mainloop()


if __name__ == "__main__":
    main()