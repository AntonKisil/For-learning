def square_rectangle(width:float,length:float):
    """Function calculates the square of a rectangle by width and length"""
    return width*length

def square_triangle(height:float,base:float):
    """Function calculates the square of a triangle by height and base"""
    return height*base/2

def square_circle(radius:float):
    """Function calculates the square of a circle by radius"""
    from math import pi
    return pi*radius**2

geometric_shape=''
while geometric_shape not in ('rectangle', 'triangle', 'circle'):
    geometric_shape=input('Enter geometric shape (rectangle, triangle or circle) : ',)
    if geometric_shape=='rectangle':
        width_rectangle=float(input('Enter width of rectangle : '))
        length_rectangle=float(input('Enter length of rectangle : '))
        print(f'Square of a rectangle : {square_rectangle(width_rectangle,length_rectangle)}')
    elif geometric_shape=='trisangle':
        height_triangle=float(input('Enter height of triangle : '))
        base_triangle=float(input('Enter base of triangle : '))
        print(f'Square of a triangle : {square_triangle(height_triangle,base_triangle)}')
    elif geometric_shape=='circle':
        radius_circle=float(input('Enter radius of circle : '))
        print('Square of a circle : {0:.2f}'.format(square_circle(radius_circle)))


