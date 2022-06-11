def square_rectangle(width:float,length:float):
    """
    The function calculates the square of a rectangle
    """
    return width*length

def square_triangle(height:float,base:float):
    """
    The function calculates the square of a triangle
    """
    return 0.5*height*base

def square_circle(radius:float):
    """
    The function calculates the square of a circle
    """
    import math
    return math.pi*math.pow(radius,2)