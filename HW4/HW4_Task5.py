number=int(input('Enter positive number : '))
if number>=0:
    fibonacci_numbers=[0,1]
    if number==0:
        print(f"""Fibonacci numbers up to the entered number:
{fibonacci_numbers[0]}""")
    elif number==1:
        print(f"""Fibonacci numbers up to the entered number:
{fibonacci_numbers}""")
    else:
        for item in range(2,number+1):
            fibonacci_numbers.append(fibonacci_numbers[item-2]+fibonacci_numbers[item-1])
        print(f"""Fibonacci numbers up to the entered number:
{fibonacci_numbers}""")
else: print('Number is negative')

