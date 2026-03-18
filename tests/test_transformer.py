import pytest
from utils.transformer import int_to_string, string_to_int, format_date, celsius_to_fahrenheit  

def test_int_to_string():
    assert int_to_string(123) == "123"

def test_empty_int_to_string():
    with pytest.raises(ValueError):
        int_to_string(None)   

def test_int_to_string_negative():
    assert int_to_string(-456) == "-456"

def test_int_to_string_letters():
    with pytest.raises(ValueError):
        int_to_string("abc")                     

def test_string_to_int():
    assert string_to_int("123") == 123

def test_string_to_int_invalid_input():
    with pytest.raises(ValueError):
        string_to_int("not a number")

def test_string_to_int_string_with_letters():
    with pytest.raises(ValueError):
        string_to_int("abc")            

def test_format_date():
    assert format_date("2024-01-15") == "January 15, 2024"

def test_format_date_invalid_input():
    with pytest.raises(ValueError):
        format_date("15-01-2024")

def test_format_date_empty_input():
    with pytest.raises(ValueError):
        format_date("")            

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40        

def test_celsius_to_fahrenheit_invalid_input():
    with pytest.raises(ValueError):
        celsius_to_fahrenheit("not a number")     
