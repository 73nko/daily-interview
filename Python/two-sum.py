###
# 21-20-2020
# Hi, here's your problem today. This problem was recently asked by Facebook:

# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.
###

def two_sum(list, k):
    seen = set()
    for num in list:
        if k - num in seen:
            return True
        seen.add(num)
    return False


print(two_sum([4, 7, 1, -3, 2], 5))
# True
