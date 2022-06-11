def number_characters(text:str):
    """
    Function calculates the number of characters included in a given string
    """
    number_characters={}
    for item in text:
        number_characters[item]=text.count(item)
    return number_characters

text=input('Enter string:')
print(f'Number of characters included in a given string : {number_characters(text)}')