###
# 13-01-2021
# Hi, here's your problem today. This problem was recently asked by Amazon:
#
# Given two arrays, write a function to compute their intersection -
# the intersection means the numbers that are in both arrays.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.
###

###
# Solution
# This problem isn't terribly difficult, but there are a lot of ways to mess up this problem,
# which makes it fun to think about.
#
# It's possible to use a combination of arrays, sets, and hashmaps here,
# and the challenge is picking the right data structure.
#
# This runs in linear time and linear space.
#
# This is a good example to look at and be careful about using built-ins. Sure, it's easy to do a one-liner like :
# set1 = set(nums1)
# set2 = set(nums2)
# return [x for x in set1 if x in set2]
# But as you can see this is already using more space than necessary,
# and the time-space analysis becomes tricky to analyze
# (it is dependent on Python's implementation of these) due to the built-ins and lambda one-liner.
###

def intersection(nums1, nums2):
    has_obj = {}
    duplicates = {}
    for i in nums1:
        has_obj[i] = 1
    for i in nums2:
        if i in has_obj:
            duplicates[i] = 1
    return duplicates.keys()


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))