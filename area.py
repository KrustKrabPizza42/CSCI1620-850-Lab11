import math

def circle(radius):

    if float(radius) <= 0:
        raise TypeError

    return math.pow(float(radius), 2) * math.pi

def square(side):

    if float(side) <= 0:
        raise TypeError

    return math.pow(float(side), 2)

def rectangle(length, width):

    if float(length) <= 0 or float(width) <= 0:
        raise TypeError

    return float(length)*float(width)

def triangle(base, height):

    if float(base) <= 0 or float(height) <=0:
        raise TypeError

    return (float(base) * float(height))/2