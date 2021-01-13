###
# 13-01-2021
# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# You are given an array of integers. Return the length of the longest increasing subsequence
# (not necessarily contiguous) in the array.
#
# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#
# The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
###

###
# Solution
# This has an exponential time complexity due to the repeated computations.
# To optimize it we can use dynamic programming and use a 1D cache of length N.
#
# Each index in this cache stores the length of the longest increasing subsequence ending at the index.
# At the end, we simply return the largest value in this cache.
###

def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)


print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))