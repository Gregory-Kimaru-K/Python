def factorial(num):
    fact = 1

    if num == 0:
        return 0
    
    if num < 0:
        num = num * -1

    while num != 0:
        fact *= num
        num -= 1

    return fact

facto = factorial(-3)
print(facto)