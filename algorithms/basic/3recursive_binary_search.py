def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            
            else:
                return recursive_binary_search(list[:midpoint], target)
            

def verify(result):
    print(f"Target found: {result}")


lst = list(range(1, 31))
tar = 28

result = recursive_binary_search(lst, tar)

verify(result)