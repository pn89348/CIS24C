def add(num1, num2):
    return num1 + num2
def diff(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
    return num1 - num2
def product(num1, num2):
    return num1 * num2
def greatest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return None