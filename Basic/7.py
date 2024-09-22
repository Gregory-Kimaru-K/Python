import math
def IsPrime(num):
    if num < 0:
        num = num*-1

    if num <= 1:
        print(f'Try number greater than 1')
        return

    i = 2

    while i < math.sqrt(num):
        if num % i == 0:
            return False
        i += 1

    return True

number = int(input("Enter a number: ")) 
checkprime = IsPrime(number)

if checkprime == True:
    print(f'{number} is a prime number')

else:
    print(f"{number} is not a prime number")