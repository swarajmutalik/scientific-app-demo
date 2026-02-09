import math

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def arcsine(x):
    return math.degrees(math.asin(x))

def arccosine(x):
    return math.degrees(math.acos(x))

def arctangent(x):
    return math.degrees(math.atan(x))

def log10(x):
    if x <= 0:
        raise ValueError("Log undefined")
    return math.log10(x)

def ln(x):
    if x <= 0:
        raise ValueError("Log undefined")
    return math.log(x)

def exponential(x):
    return math.exp(x)

def factorial(n):
    if n < 0 or not float(n).is_integer():
        raise ValueError("Factorial undefined")
    return math.factorial(int(n))
