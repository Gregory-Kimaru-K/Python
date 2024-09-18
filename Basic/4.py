def fibonnacci(num):
    fib_list = [0, 1]

    i = 2
    while i <= num:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        i += 1
    
    return fib_list

fibo = fibonnacci(10)

print(fibo)