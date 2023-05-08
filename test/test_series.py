import pytest
from series import fibonacci
from series import lucas
from series import sum_series
from series import sum_series_list_delete


# fibonacci tests

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

def test_fibonacci_five():
    actual = fibonacci(50)
    expected = 12586269025
    assert actual == expected

def test_fibonacci_six():
    n = -1
    actual = fibonacci(n)
    respons = "there is no fibonacci number for this {} {}"
    expected = respons.format(type(n),n)
    assert actual == expected

def test_fibonacci_seven():
    n = "1"
    actual = fibonacci(n)
    respons = "there is no fibonacci number for this {} {}"
    expected = respons.format(type(n),n)
    assert actual == expected

# lucas tests

def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_four():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_five():
    actual = lucas(13)
    expected = 521
    assert actual == expected

def test_lucas_six():
    n = -1
    actual = lucas(n)
    respons = "there is no lucas number for this {} {}"
    expected = respons.format(type(n),n)
    assert actual == expected

def test_lucas_seven():
    n = "1"
    actual = lucas(n)
    respons = "there is no lucas number for this {} {}"
    expected = respons.format(type(n),n)
    assert actual == expected
