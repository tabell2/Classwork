import turtle


def digit_to_roman(digit):
    roman_map = {
        '0': '',  # 0 -> nothing (blank)
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


def parse_date(date_str):
    date_str = date_str.strip()

    # Split by / or -
    if '/' in date_str:
        parts = date_str.split('/')
    elif '-' in date_str:
        parts = date_str.split('-')
    else:
        raise ValueError("Invalid date format. Use MM/DD/YYYY or MM-DD-YYYY")

    if len(parts) != 3:
        raise ValueError("Invalid date format. Use MM/DD/YYYY or MM-DD-YYYY")

    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])

    # Validate
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    if year < 0 or year > 9999:
        raise ValueError("Year must be between 0 and 9999")

    return month, day, year


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
    x = start_x

    for i, char in enumerate(roman_str):
        draw_letter(t, char, x, y)
        if i < len(roman_str) - 1:
            if char in ['X', 'V'] and roman_str[i + 1] == 'I':
                x += 35
            else:
                x += 25


def draw_dash(t, x, y):
    t.penup()
    t.goto(x - 15, y + 30)
    t.pendown()
    t.goto(x + 15, y + 30)


def draw_date(month, day, year, screen, t):
    t.clear()

    # Convert date to string with leading zeros
    date_str = f"{month:02d}/{day:02d}/{year:04d}"

    # Convert month digits
    if month == 10:
        month_roman = 'X'
    elif month == 11:
        month_roman = 'XI'
    elif month == 12:
        month_roman = 'XII'
    else:
        # For other months, convert each digit separately
        month_digit1 = digit_to_roman(date_str[0])
        month_digit2 = digit_to_roman(date_str[1])
        month_roman = None

    # Convert day and year digits
    day_digit1 = digit_to_roman(date_str[3])
    day_digit2 = digit_to_roman(date_str[4])
    year_digit1 = digit_to_roman(date_str[6])
    year_digit2 = digit_to_roman(date_str[7])
    year_digit3 = digit_to_roman(date_str[8])
    year_digit4 = digit_to_roman(date_str[9])

    t.speed(1)
    t.pensize(3)
    t.color("black")

    # Calculate starting positions
    max_width = 35 * 4
    gap = -20
    dash_space = 90

    if month_roman:
        month_width = len(month_roman) * 35
        total_width = month_width + gap + dash_space + max_width + gap + max_width + gap + dash_space + max_width * 4 + gap * 3
    else:
        total_width = max_width + gap + max_width + gap + dash_space + max_width + gap + max_width + gap + dash_space + max_width * 4 + gap * 3

    start_x = -total_width / 2

    y_pos = -30

    # Draw month
    x_pos = start_x
    if month_roman:
        draw_roman_numeral(t, month_roman, x_pos, y_pos)
        x_pos += max_width + gap
    else:
        draw_roman_numeral(t, month_digit1, x_pos, y_pos)
        x_pos += max_width + gap
        draw_roman_numeral(t, month_digit2, x_pos, y_pos)
        x_pos += max_width + gap

    # Draw first dash
    x_pos += dash_space / 6
    draw_dash(t, x_pos, y_pos)

    # Draw day
    x_pos += dash_space * 5 / 6 + gap
    draw_roman_numeral(t, day_digit1, x_pos, y_pos)
    x_pos += max_width + gap
    draw_roman_numeral(t, day_digit2, x_pos, y_pos)

    # Draw second dash
    x_pos += max_width + dash_space / 6
    draw_dash(t, x_pos, y_pos)

    # Draw year
    x_pos += dash_space * 5 / 6 + gap
    draw_roman_numeral(t, year_digit1, x_pos, y_pos)
    x_pos += max_width + gap
    draw_roman_numeral(t, year_digit2, x_pos, y_pos)
    x_pos += max_width + gap
    draw_roman_numeral(t, year_digit3, x_pos, y_pos)
    x_pos += max_width + gap
    draw_roman_numeral(t, year_digit4, x_pos, y_pos)

    # Hide turtle
    t.hideturtle()


def main():
    # Set up turtle screen
    screen = turtle.Screen()
    screen.setup(width=1200, height=500)
    screen.title("Roman Numeral Date")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()

    # Display instructions
    t.penup()
    t.goto(0, 100)
    t.write("Roman Numeral Date Converter", align="center", font=("Arial", 24, "bold"))
    t.goto(0, 60)
    t.write("Enter date below", align="center", font=("Arial", 16, "normal"))

    while True:
        try:
            # Get date input from user
            date_input = screen.textinput("Date Input", "Enter date:")

            if date_input is None:
                break

            month, day, year = parse_date(date_input)

            # Draw the date
            draw_date(month, day, year, screen, t)
            break

        except ValueError as e:
            # Show error message
            result = screen.textinput("Error", f"Invalid date format. Try again?\n(Enter 'yes' to continue)")
            if result is None or result.lower() != 'yes':
                break
        except Exception:
            break

    # Keep window open
    screen.mainloop()


if __name__ == "__main__":
    main()