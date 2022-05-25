input_number=int(input('Enter a number: '))
if input_number<0:
    print('Enter a positive integer')
elif input_number==0:
    print('Factorial of 0 = 1')
else:
    factorial_input_number=1
    for index in range(1,input_number+1):
        factorial_input_number*=index
    print(f'Factorial of {input_number} = {factorial_input_number}')
