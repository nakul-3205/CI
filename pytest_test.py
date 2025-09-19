# pytest_test.py
from app import square

def test_square_positive():
    assert square(2) == 4
    assert square(5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-3) == 9
