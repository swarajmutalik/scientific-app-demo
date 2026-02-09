from arithmetic import *

def test_modulus():
    assert modulus(10, 3) == 1

def test_floor_divide():
    assert floor_divide(10, 3) == 3

def test_negate():
    assert negate(5) == -5
