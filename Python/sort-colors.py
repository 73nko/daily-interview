###
# 31-12-2020
# Hi, here's your problem today. This problem was recently asked by Apple:
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library’s sort function for this problem.
#
# Can you do this in a single pass?
###


def sort_colors(nums):
    p0 = curr = 0
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            # swap p0 with curr
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            # swap p2 with curr
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1


numbers = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(numbers)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

sort_colors(numbers)
print("After Sort: ")
print(numbers)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]