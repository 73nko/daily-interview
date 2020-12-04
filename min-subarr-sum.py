###
# 04-12-2020
# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given an array of n positive integers and a positive integer s, find the minimal
# length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
###
class Solution:
    def minSubArrayLen(self, nums, s):
        l, r = 0, -1
        sum = 0
        res = len(nums) + 1
        while(l < len(nums)):
            if (sum < s) and (r + 1 < len(nums)):
                # if sum is smaller, keep moving right index to increase window
                r += 1
                sum += nums[r]
            else:
                # if sum >= s, move left index to shrink window
                sum -= nums[l]
                l += 1

            if sum >= s:
                # if sum is found
                res = min(res, r - l + 1)
        if(res == len(nums) + 1):
            # if no solution is found
            return 0
        return res


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
