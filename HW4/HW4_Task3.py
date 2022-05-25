list_input=[int(item) for item in input("Enter the list items : ").split()]
for odd_number in list_input:
    if odd_number%2!=0:
        condition=True
        print('The list contains odd numbers')
        break
else: print('The list doesn`t contain odd numbers')