print('All odd numbers less than 100.\n\nVariant of the code using the continue operator:')
# Variant of the code using the continue operator
for odd_number in range(100):
    if odd_number%2==0: continue
    else: print(odd_number,end=" ")
# Variant of the code without the continue operator  
print('\n\nVariant of the code without the continue operator:')
for odd_number in range(1,100,2):
    print(odd_number,end=" ")
