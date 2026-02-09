from statistics import *

from statistics import standard_deviation

def test_mean():
    assert mean([2, 4, 6]) == 4

def test_variance():
    assert variance([2, 4, 6]) == 2.67

def test_standard_deviation():
    assert round(standard_deviation([2, 4, 6]), 2) == 1.63
