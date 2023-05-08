import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series
from series.series import sum_series_list_delete


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

# sum_series tests

def test_sum_series_one():
    actual = sum_series(5)
    expected = 5
    sum_series_list_delete()
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(5,5)
    expected = 20
    sum_series_list_delete()
    assert actual == expected

def test_sum_series_three():
    actual = sum_series(5,5,5)
    sum_series_list_delete()
    expected = 40
    assert actual == expected

def test_sum_series_four():
    actual = sum_series("5",5,5)
    sum_series_list_delete()
    expected = "one of the pram isn't an int"
    assert actual == expected

def test_sum_series_five():
    actual = sum_series(2,2,1)
    sum_series_list_delete()
    expected = 3
    assert actual == expected

def test_sum_series_six():
    actual = sum_series(3,0,-1)
    sum_series_list_delete()
    expected = -2
    assert actual == expected