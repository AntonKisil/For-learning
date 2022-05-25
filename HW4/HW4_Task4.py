list_numbers=[int(item) for item in input("Enter the list : ").split()]
print(f'Data type was : {type(list_numbers[len(list_numbers)-1])}')
for item in range(len(list_numbers)):
    list_numbers[item]=float(list_numbers[item])
print(f'Data type became : {type(list_numbers[len(list_numbers)-1])}')