import math 

def power(a,b):
    return a ** b

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def square_root(a):
    if a < 0:
        raise ValueError("Negative Input")
    return math.sqrt(a)
