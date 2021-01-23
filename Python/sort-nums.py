###
# 20-11-2020
# Hi, here's your problem today. This problem was recently asked by Google:

# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
# def sortNums(nums):
#   # Fill this in.

# print sortNums([3, 3, 2, 1, 3, 2, 1])
# # [1, 1, 2, 2, 3, 3, 3]

# Challenge: Try sorting the list using constant space.
###

def sortNums(nums):
    one_idx = 0
    three_idx = len(nums) - 1
    idx = 0
    while idx <= three_idx:
        if nums[idx] == 1:
            nums[idx], nums[one_idx] = nums[one_idx], nums[idx]
            idx += 1
            one_idx += 1
        elif nums[idx] == 2:
            idx += 1
        elif nums[idx] == 3:
            nums[idx], nums[three_idx] = nums[three_idx], nums[idx]
            three_idx -= 1
    return nums


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
