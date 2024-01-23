# recursion task 7

def _recursive_find_2nd_largest(arg, max_1, max_2, i):
    if len(arg) == i:
        return max_2
    current = arg[i]
    if current >= max_1:
        max_2 = max_1
        max_1 = current
    if current < max_1 and current > max_2:
        max_2 = current
    return _recursive_find_2nd_largest(arg, max_1, max_2, i+1)

def recursive_find_2nd_largest(arg):
    if len(arg) < 2:
        return None
    max_1 = max(arg[0], arg[1])
    max_2 = min(arg[0], arg[1])
    return _recursive_find_2nd_largest(arg, max_1, max_2, 2)

arg =  [2,3,5,4]
print(recursive_find_2nd_largest(arg))
arg =  [2,5,4,3,5]
print(recursive_find_2nd_largest(arg))
arg =  [2,5]
print(recursive_find_2nd_largest(arg))
