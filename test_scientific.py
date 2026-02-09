from scientific import *

def test_sine():
    assert round(sine(30), 2) == 0.5

def test_cosine():
    assert round(cosine(60), 2) == 0.5

def test_log10():
    assert log10(100) == 2

def test_factorial():
    assert factorial(5) == 120
