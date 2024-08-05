import pytest
from list_square_lc import list_square

def test_1():
    assert list_square([1,2,3])==[1,4,9]

def test_2():
    assert list_square([-1,-2,0])==[1,4,0]

def test_3():
    assert list_square([])==[]

