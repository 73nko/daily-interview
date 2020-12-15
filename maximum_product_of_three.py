###
# 15-12-2020
# Hi, here's your problem today. This problem was recently asked by Microsoft:

# You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

# Example:

# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
###

def maximum_product_of_three(lst):
    lst.sort()
    third_largest, second_largest, first_largest = lst[-3], lst[-2], lst[-1]
    first_smallest, second_smallest = lst[0], lst[1]
    return max(third_largest * second_largest * first_largest,
               first_largest * first_smallest * second_smallest)


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
