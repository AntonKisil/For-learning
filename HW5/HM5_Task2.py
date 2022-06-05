numbers_divisible_2=tuple()
numbers_divisible_3=tuple()
numbers_notdivisible_2and3=tuple()
for number in range(1,10):
    if number%2!=0 and number%3!=0:
        numbers_notdivisible_2and3+=number,
    else:
        if number%2==0:
            numbers_divisible_2+=number,
        if number%3==0:
            numbers_divisible_3+=number,
print(f'\
In the range from 1 to 10:\n\
- even numbers that are divisible by 2 : {numbers_divisible_2}\n\
- odd numbers, which are divisible by 3 : {numbers_divisible_3}\n\
- numbers that are not divisible by 2 and 3 : {numbers_notdivisible_2and3}')