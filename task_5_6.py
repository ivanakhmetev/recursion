"""recursion task 5 and 6"""

def recursive_print_even_el(arg: list, start: int):
    '''print even numbers'''
    if start < len(arg) and arg[start] % 2 == 0:
        print(arg[start])
    new_start = start + 1
    if start < len(arg):
        recursive_print_even_el(arg, new_start)

recursive_print_even_el([1,2,3,4,5,6], 10)

def recursive_print_even_indexs(arg: list):
    return _recursive_print_even_indexs(arg, 0)

def _recursive_print_even_indexs(arg: list, start: int) -> None:
    if start == len(arg):
        return
    print(arg[start])
    _recursive_print_even_indexs(arg, start + 2)

print(recursive_print_even_indexs([0,1,0,2,0,3]))
    
