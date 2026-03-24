import pytest
from utils.parser import parse_to_machine_format, parse_db_record, parse_user_input      

def test_parse_user_input_valid_string():
    assert parse_user_input("  Hello World  ") == "Hello World"

def test_parse_user_input_none():
    with pytest.raises(ValueError):
        parse_user_input(None)

def test_parse_user_input_empty_string():
    with pytest.raises(ValueError):
        parse_user_input("")    

def test_parse_to_machine_format_valid_data():
    input_data = {"first_name": " John ", "age": 25}
    expected_output = {"first_name": "john", "age": 25}
    assert parse_to_machine_format(input_data) == expected_output       

def test_parse_to_machine_format_invalid_input():
    with pytest.raises(ValueError):
        parse_to_machine_format("not a dictionary") 

def test_parse_to_machine_format_empty_dictionary():
    with pytest.raises(ValueError):
        parse_to_machine_format({})       

def test_parse_db_record_valid_data():
    input_data = {"first_name": "john", "age": 25}
    expected_output = {"first_name": "John", "age": "25"}
    assert parse_db_record(input_data) == expected_output  

def test_parse_db_record_invalid_input():
    with pytest.raises(ValueError):
        parse_db_record("not a dictionary")

def test_parse_db_record_empty_dictionary():
    with pytest.raises(ValueError):
        parse_db_record({})     

def test_parse_db_record_none_values():
    result = parse_db_record({"name": None, "age": 25})
    assert result["name"] == ""    # None becomes empty string
    assert result["age"] == "25"
