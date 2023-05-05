import pytest
from series import fibonacci

def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected