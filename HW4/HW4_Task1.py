print('All even numbers less than 100.\n\nVariant of the code using the while loop:')
# Variant of the code using the while loop
even_number=0
while even_number<98:
    even_number+=2
    print(even_number,end=" ")
# Variant of the code using the for loop    
print('\n\nVariant of the code using the for loop:')
for even_number in range(2,99,2):
    print(even_number,end=" ")