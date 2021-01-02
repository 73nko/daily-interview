###
# 02--12-2021
# Hi, here's your problem today. This problem was recently asked by Twitter:
#
# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c)
# in nums such that a + b + c = 0.
# Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.
#
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]
###

def three_sum(nums):
    results = []
    nums.sort()
    length = len(nums)
    # Range is length - 2 because we need at least
    # 3 numbers to continue
    for i in range(length - 2):
        # The sum of 3 positive numbers will always be > 0.
        if nums[i] > 0:
            break
        # If nums[i] == nums[i - 1], it's a duplicate
        # element and we don't need to check.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, length - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                results.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return results


# Test Program
solution = [1, -2, 1, 0, 5]

print(three_sum(solution))