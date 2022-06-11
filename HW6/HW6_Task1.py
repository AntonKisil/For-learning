def arithmeticMean(*args: float):
    """
    This function calculate arithmetic mean
    """
    return sum(args)/len(args)

numbers=[float(item) for item in input('Enter the numbers :').split()]
arithmetic_mean=arithmeticMean(*numbers)
print(f'Arithmetic mean = {arithmetic_mean}')
