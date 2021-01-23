###
# 13-01-2021
# Hi, here's your problem today. This problem was recently asked by Amazon:
#
# You are given an array of integers. Return an array of the same size where the element at each index
# is the product of all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
###

###
# Solution
# If division was allowed, the problem would be quite simple.
# We just calculate the product of all the elements in the array first,
# and then do a second pass where we divide the total product by the current element.
#
# Without the use of division, it is easy to find a solution by realizing
# that the element at index i is simply the product of all the numbers before i,
# and all the numbers after i. To do this efficiently, we will generate a list of these "prefix" products,
# and "suffix" products for each element. Then, the output at each index is simply the prefix and suffix products
# of the element multiplied together.
###

def products(nums):
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


print(products([1, 2, 3, 4, 5]))