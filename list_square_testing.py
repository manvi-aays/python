import pytest
from list_square import list_squares

def test_case_1():
    assert list_squares([1, 2, 3, 4]) == [1, 4, 9, 16]

def test_case_2():
    assert list_squares([]) == []
    
def test_case_3():
    assert list_squares([-1, -2, -3, 0]) == [1, 4, 9, 0]
