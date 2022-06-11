from turtle import width
import HW7_Task3_calc_square
figure=input('Enter a figure : ')
if figure=='rectangle':
    width=float(input('Enter width : '))
    length=float(input('Enter length : '))
    print('Square of rectangle : ',HW7_Task3_calc_square.square_rectangle(width,length))
elif figure=='triangle':
    height=float(input('Enter height : '))
    base=float(input('Enter base : '))
    print('Squre of triangle : ',HW7_Task3_calc_square.square_triangle(height,base))
elif figure=='circle':
    radius=float(input('Enter radius : '))
    print('Square of circle : ',HW7_Task3_calc_square.square_circle(radius))
else: print('Figure entered incorrectly')    

