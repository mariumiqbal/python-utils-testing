def add(a, b):
    # return sum of a and b
    return a + b

def subtract(a, b):
    # return a minus b
    return a-b

def multiply(a, b):
    # return a multiplied by b
    return a*b

def divide(a, b):
    # return a divided by b
    # hint: what happens if b is 0?
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b