"""recursion task 3 and 4"""

def recursive_get_len_pop_all(arg: list) -> int:
    """# 3 len(list)"""
    if not arg:
        return 0
    arg.pop(0)
    return recursive_get_len_pop_all(arg) + 1

a = list('abs')
b = []
assert recursive_get_len_pop_all(a) == 3
assert recursive_get_len_pop_all(b) == 0

def recursive_is_palindrome(arg: str, start: int, end: int) -> bool or None:
    '''#4 is palindrome?'''
    if start == end:
        return True
    if arg[start] != arg[end]:
        return False
    if start < end + 1:
        return recursive_is_palindrome(arg, start + 1, end - 1)
    return None

assert recursive_is_palindrome('aboba', 0, 0) is True
assert recursive_is_palindrome('aboba', 1, 3) is True
assert recursive_is_palindrome('aboba', 0, 4) is True
assert recursive_is_palindrome('aaaba', 0, 4) is False
assert recursive_is_palindrome('aaaba', 2, -1) is None
