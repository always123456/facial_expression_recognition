import math

def average_string(number_string):
    # else : 在所有的except不执行的情况下，执行else
    # finally : 最终一定执行的子句
    try:
        numbers = [float(n) for n in number_string.split()]
    except ValueError:
        total = math.nan
        values = 1
    else:
        total = sum(numbers)
        values = len(numbers)

    try:
        average = total / values
    except ZeroDivisionError:
        average = math.inf
    
    return average

while True:
    number_string = input("Enter list of numbers separated by spaces: \n")
    print(average_string(number_string))


