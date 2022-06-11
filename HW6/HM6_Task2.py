
# First version of code using if statement
def largestNumber1(a: float,b: float):
    """Function returns the lagest number of two numbers"""
    if a>b:
        return a
    else:
        return b

# Second version of code using the built-in function
def largestNumber2(a: float,b: float):
    """Function returns the lagest number of two numbers"""
    return max(a,b)
    