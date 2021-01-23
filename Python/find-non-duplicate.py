###
# 21-11-2020
# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given a list of numbers, where every number shows up twice except for one number, find that one number.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
###

from functools import reduce


def singleNumber(nums):
    return reduce(lambda acc, n: acc ^ n, nums)


print(singleNumber([4, 3, 2, 4, 1, 1, 8, 3, 2, 8, 56]))
# 56
