# 1. n ^ m
def recursive_raise_to_power(N: int, M: int):
    if M == 0:
        return 1
    if M == 1:
        return N
    if M != 0 and M != 1 and M > 0:
        return N * recursive_raise_to_power(N, M - 1)
    if M != 0 and M != 1 and M < 0:
        return 1 / (N * recursive_raise_to_power(N, -M  - 1))

print(recursive_raise_to_power(2,-2))
print(recursive_raise_to_power(3,4))

# 2. 123 to 1 + 2 + 3
def recursive_sum_digits(num: int):
    if num < 0:
        num = - num
    num_str = str(num)
    count_digits = len(num_str)
    if count_digits == 1:
        return num
    if count_digits != 1:
        return int(num_str[0]) + recursive_sum_digits(int(num_str[1:]))

print(recursive_sum_digits(3))
print(recursive_sum_digits(-345))
print(recursive_sum_digits(4444))
