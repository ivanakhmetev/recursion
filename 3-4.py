# 3 len(list)

class my_list(list):

    def __init__(self, arg):
        super().__init__(arg)
    
    def my_pop(self):
        super().pop()


def recursive_get_len_pop_all(arg: my_list):
    try:
        arg.my_pop()
        return recursive_get_len_pop_all(arg) + 1
    except:
        return 0

a = my_list('abs')
print(recursive_get_len_pop_all(a))

#4 is palindrome?

def recursive_is_palindrome(arg: str):
    if len(arg) == 1:
        return True
    if len(arg) == 2:
        return arg[0] == arg[-1]
    if len(arg) > 2:
        return arg[0] == arg[-1] and recursive_is_palindrome(arg[1:-1])


print(recursive_is_palindrome('a'))
print(recursive_is_palindrome('aaba'))
print(recursive_is_palindrome('baabs'))
print(recursive_is_palindrome('aba'))
print(recursive_is_palindrome('aboba'))

