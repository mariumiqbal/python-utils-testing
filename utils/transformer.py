from datetime import datetime

def int_to_string(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return str(value)

def string_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Input must be a valid integer string")
    
def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        raise ValueError("Input must be in the format YYYY-MM-DD")

def celsius_to_fahrenheit(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Input must be a number")
    return (temp * 9/5) + 32
    