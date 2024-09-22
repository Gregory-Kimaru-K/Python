def FizzBuzz(num):
    num += 1
    lst = []
    for num in range(1, num):
        lst.append(num)
    
    i = 0

    while i < len(lst):
        if lst[i] % 3 == 0 and lst[i] % 5 == 0:
            print(f'{lst[i]} gave FIZZBUZZ')
        if lst[i] % 3 == 0:
            print(f'{lst[i]} gave FIZZ')
        if lst[i] % 5 == 0:
            print(f'{lst[i]} gave BUZZ')
        i += 1

FizzBuzz(50)