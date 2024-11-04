a = [2, 5, 4, 8, 9, 6]

max_num = None
for number in range(len(a)):
    if max_num == None:
        max_num = a[number]

    elif a[number] > max_num:
        max_num = a[number]

print(max_num)