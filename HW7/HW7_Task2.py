from random import randint
number=randint(1,100)
input_number=int(input('Gues the number : '))
if input_number==number:
    print(f'Congratulations! It is {number}')
else:
    done=True
    while done:
        if input_number>number:
            input_number=int(input('Try to choose a smaller number : '))
        elif input_number<number:
            input_number=int(input('Try to choose a larger number : '))
        else:
            print(f'Congratulations! It is {number}')
            done=False
        

        
