import turtle


def digit_to_roman(digit):
    """Convert a single digit (0-9) to Roman numeral"""
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
        '9': 'IX'
    }
    return roman_map.get(str(digit), '')


def parse_date(date_str):
    """Parse date string and return (month, day, year)"""
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
    """Draw a single Roman numeral letter at position"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)  # Face up

    height = 60
    width = 30

    if letter == 'I':
        # Draw vertical line
        t.forward(height)

    elif letter == 'V':
        # Draw V shape - same height as I, just two diagonals
        t.penup()
        t.goto(x, y + height)
        t.pendown()
        t.goto(x + width / 2, y)  # Diagonal down to bottom center
        t.goto(x + width, y + height)  # Diagonal up to top right

    elif letter == 'X':
        # Draw X shape - same height as I and V
        t.penup()
        t.goto(x, y + height)
        t.pendown()
        t.goto(x + width, y)  # Diagonal from top-left to bottom-right
        t.penup()
        t.goto(x + width, y + height)
        t.pendown()
        t.goto(x, y)  # Diagonal from top-right to bottom-left


def draw_roman_numeral(t, roman_str, start_x, y):
    """Draw a complete Roman numeral string"""
    x = start_x

    for i, char in enumerate(roman_str):
        draw_letter(t, char, x, y)
        # Add extra space after X or V if followed by I
        if i < len(roman_str) - 1:
            if char in ['X', 'V'] and roman_str[i + 1] == 'I':
                x += 35  # More space between X/V and I
            else:
                x += 25  # Normal spacing between same type letters


def draw_dash(t, x, y):
    """Draw a horizontal dash"""
    t.penup()
    t.goto(x - 15, y + 30)
    t.pendown()
    t.goto(x + 15, y + 30)


def draw_date(month, day, year, screen, t):
    """Draw the date with each digit as a Roman numeral using turtle"""
    # Clear screen
    t.clear()

    # Convert date to string with leading zeros
    date_str = f"{month:02d}/{day:02d}/{year:04d}"

    # Convert month digits - special handling for 10, 11, 12
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
        month_roman = None  # Will draw separately

    # Convert day and year digits
    day_digit1 = digit_to_roman(date_str[3])
    day_digit2 = digit_to_roman(date_str[4])
    year_digit1 = digit_to_roman(date_str[6])
    year_digit2 = digit_to_roman(date_str[7])
    year_digit3 = digit_to_roman(date_str[8])
    year_digit4 = digit_to_roman(date_str[9])

    t.speed(1)  # Slow speed
    t.pensize(3)
    t.color("darkblue")

    # Calculate starting positions
    max_width = 35 * 4  # Maximum width for a digit
    gap = -20  # Negative gap to bring digit groups closer together
    dash_space = 90  # Increased space for dashes

    # Calculate total width more accurately based on actual drawing positions
    if month_roman:
        # Month is single numeral (X, XI, XII) - approximately 1-3 letters wide
        month_width = len(month_roman) * 35
        total_width = month_width + gap + dash_space + max_width + gap + max_width + gap + dash_space + max_width * 4 + gap * 3
    else:
        # Month is two digits
        total_width = max_width + gap + max_width + gap + dash_space + max_width + gap + max_width + gap + dash_space + max_width * 4 + gap * 3

    start_x = -total_width / 2

    y_pos = -30

    # Draw month
    x_pos = start_x
    if month_roman:
        # Draw as single numeral (X, XI, XII)
        draw_roman_numeral(t, month_roman, x_pos, y_pos)
        x_pos += max_width + gap
    else:
        # Draw as two separate digits
        draw_roman_numeral(t, month_digit1, x_pos, y_pos)
        x_pos += max_width + gap
        draw_roman_numeral(t, month_digit2, x_pos, y_pos)
        x_pos += max_width + gap

    # Draw first dash
    x_pos += dash_space / 6  # Less space before dash
    draw_dash(t, x_pos, y_pos)

    # Draw day (with extra space after dash)
    x_pos += dash_space * 5 / 6 + gap  # More space after dash
    draw_roman_numeral(t, day_digit1, x_pos, y_pos)
    x_pos += max_width + gap
    draw_roman_numeral(t, day_digit2, x_pos, y_pos)

    # Draw second dash
    x_pos += max_width + dash_space / 6  # Less space before dash
    draw_dash(t, x_pos, y_pos)

    # Draw year (with extra space after dash)
    x_pos += dash_space * 5 / 6 + gap  # More space after dash
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
    screen.title("Roman Numeral Date - Enter date in format MM/DD/YYYY")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()

    # Display instructions
    t.penup()
    t.goto(0, 100)
    t.write("Roman Numeral Date Converter", align="center", font=("Arial", 24, "bold"))
    t.goto(0, 60)
    t.write("Enter date below", align="center", font=("Arial", 16, "normal"))
    t.goto(0, 30)
    t.write("Format: MM/DD/YYYY or MM-DD-YYYY", align="center", font=("Arial", 14, "normal"))
    t.goto(0, 0)
    t.write("Example: 12/25/2024", align="center", font=("Arial", 14, "normal"))

    while True:
        try:
            # Get date input from user
            date_input = screen.textinput("Date Input", "Enter date (MM/DD/YYYY or MM-DD-YYYY):")

            if date_input is None:  # User cancelled
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