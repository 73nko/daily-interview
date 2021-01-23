###
# 20-01-2021
# Hi, here's your problem today. This problem was recently asked by LinkedIn:
#
# Write a function that reverses the digits a 32-bit signed integer, x.
# Assume that the environment can only store integers within the 32-bit signed integer range,
# [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.
#
# Example:
# Input: 123
# Output: 321
###
def reverse(x):
    sign = [1, -1][x < 0]
    reversed_str = sign * int(str(abs(x))[::-1])
    return reversed_str if -(2 ** 31) - 1 < reversed_str < 2 ** 31 else 0


print(reverse(123))