###
# 28-11-2020
# Hi, here's your problem today. This problem was recently asked by Uber:

# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 52 + 122 = 132.
###

def findPythagoreanTriplets(nums):
    squares = set([n**2 for n in nums])

    for a in nums:
        for b in nums:
            if a**2 + b**2 in squares:
                return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
