###
# 13-01-2021
# Hi, here's your problem today. This problem was recently asked by Facebook:
#
# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.
###


###
# Solution
# The question can be solved by iterating through the list of numbers, while keeping track of the last number.
#
# For the first number in the list we set low and high to that value. For every value we see after
# if that number is more than 1 greater than high, that means it is no longer consecutive so we write the range low ->
# high to our ranges list. low is set to the current n in that iteration as it is the
# new lowest number in the next range.
#
# We then set high to the current number we see regardless as it is the highest number we know.
# After we finish iterating the input list we still have our last range that has not been written into ranges,
# so we write the last range in and return the list as our solution.
#
# The time complexity of this problem would be O(n) as each number in the list needs to be processed.
# The space complexity of this problem is also O(n),
# as in the worst case you would need to add every number to its own range.
###

def find_ranges(nums):
    if not nums:
        return []
    ranges = []
    low = nums[0]
    high = nums[0]
    for n in nums:
        if high + 1 < n:
            ranges.append(str(low) + "->" + str(high))
            low = n
        high = n
    ranges.append(str(low) + "->" + str(high))
    return ranges


print(find_ranges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))