import pytest

from utils.calculator import add, subtract, multiply, divide


def test_add_positive_numbers():
    assert add(2,3) == 5

def test_add_negative_numbers():
    assert add(-1,1) == 0

def test_add_zeros():
    assert add(0,0) == 0

def test_subtract_positive_numbers():
    assert subtract(5,3) == 2

def test_subtract_negative_numbers():
    assert subtract(-1,1) == -2

def test_subtract_zeros():
    assert subtract(0,0) == 0

def test_multiply_positive_numbers():
    assert multiply(2,3) == 6

def test_multiply_negative_numbers():
    assert multiply(-1,1) == -1

def test_multiply_zeros():
    assert multiply(0,0) == 0

def test_divide_positive_numbers():
    assert divide(6,3) == 2

def test_divide_negative_numbers():
    assert divide(-6,3) == -2

def test_divide_zeros():
    assert divide(0,1) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1,0)