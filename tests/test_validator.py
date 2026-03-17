import pytest

from utils.validator import validate_email, validate_password, validate_phone, validate_age

def test_valid_email():
    assert validate_email("abc@gmail.com") == True

def test_invalid_email():
    with pytest.raises(ValueError):
        validate_email("invalid-email")

def test_valid_phone_number_with_dashes():
    assert validate_phone("123-456-7890") == True

def test_valid_phone_number():
    assert validate_phone("1234567890") == True         

def test_invalid_phone_number():
    with pytest.raises(ValueError):
        validate_phone("123-456-789")

def test_valid_password():
    assert validate_password("SecurePass123!") == True

def test_invalid_password():
    with pytest.raises(ValueError):
        validate_password("weak")

def test_valid_age():
    assert validate_age(25) == True

def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age(-5)

def test_empty_email():
    with pytest.raises(ValueError, match="Email cannot be empty"):
        validate_email("")

def test_email_missing_dot():
    with pytest.raises(ValueError, match="Email must contain a dot after @"):
        validate_email("abc@gmail")

def test_email_only_at_symbol():
    with pytest.raises(ValueError, match="Email must contain a dot after @"):
        validate_email("@")

def test_password_too_short():
    with pytest.raises(ValueError, match="Password must be at least 8 characters long"):
        validate_password("short")

def test_password_with_no_numbers():
    with pytest.raises(ValueError, match="Password must contain at least one number"):
        validate_password("abcdefgh")

def test_age_under_18():
    with pytest.raises(ValueError, match="Age must be at least 18"):
        validate_age(15)

def test_age_over_120():
    with pytest.raises(ValueError, match="Age must be at most 120"):
        validate_age(150)