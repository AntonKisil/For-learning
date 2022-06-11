import HW7_Task1_calculator
a=float(input('Number : '))
action=' '
action=input('Action (+, -, *, /) : ')
b=float(input('Number : '))
if action=='+':
    print(f'Result : {HW7_Task1_calculator.add(a,b)}')
elif action=='-':
    print(f'Result : {HW7_Task1_calculator.sub(a,b)}')
elif action=='*':
    print(f'Result : {HW7_Task1_calculator.mult(a,b)}')
elif action=='/':
    print(f'Result : {HW7_Task1_calculator.div(a,b)}')

