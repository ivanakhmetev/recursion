"""recursion task 5 and 6"""

def recursive_print_even_el(arg: list, start: int):
    '''print even numbers'''
    if start < len(arg) and arg[start] % 2 == 0:
        print(arg[start])
    new_start = start + 1
    if start < len(arg):
        recursive_print_even_el(arg, new_start)

recursive_print_even_el([1,2,3,4,5,6], 0)

def recursive_print_even_idx(arg: list, start: int):
    '''print at even idx'''
    if start % 2 == 0:
        print(arg[start])
    new_start = start + 1
    if start < len(arg) - 1:
        recursive_print_even_idx(arg, new_start)

recursive_print_even_idx([0,1,0,2,0,3], 0)
    
