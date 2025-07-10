import math

def circle(radius):

    if float(radius) <= 0:
        raise TypeError

    return round(math.pi * (math.pow(float(radius), 2)), 2)

def square(side):

    if float(side) <= 0:
        raise TypeError

    return round(math.pow(float(side), 2), 2)

def rectangle(length, width):

    if float(length) <= 0 or float(width) <= 0:
        raise TypeError

    return round(float(length)*float(width), 2)

def triangle(base, height):

    if float(base) <= 0 or float(height) <=0:
        raise TypeError

    return round((float(base) * float(height))/2, 2)