import re

def validate_email(email):
    if not email:                          # empty check
        raise ValueError("Email cannot be empty")
    if "@" not in email:                   # check @
        raise ValueError("Email must contain @")
    at_index = email.index("@")
    if "." not in email[at_index:]:        # check dot after @
        raise ValueError("Email must contain a dot after @")
    return True

def validate_password(password):
 
    if not password:
        raise ValueError("Password cannot be empty")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one number")
    return True

def validate_phone(phone):

    if not phone:
        raise ValueError("Phone number cannot be empty")
    if not re.match(r"^\d{10}$|^\d{3}-\d{3}-\d{4}$", phone):
        raise ValueError("Phone number must be 10 digits or in format XXX-XXX-XXXX")
    return True

def validate_age(age):

    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 18:
        raise ValueError("Age must be at least 18")
    if age > 120:
        raise ValueError("Age must be at most 120")
    return True