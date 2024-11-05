def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        
        elif list[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")

    else:
        print("Target not found in list")


lst = list(range(1, 31))
tar = 20

result = binary_search(lst, tar)

verify(result)