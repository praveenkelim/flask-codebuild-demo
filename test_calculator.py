from calculator import *

def test_add():
    assert add(5, 2) == 7

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(5, 2) == 10

def test_divide():
    assert divide(10, 2) == 5