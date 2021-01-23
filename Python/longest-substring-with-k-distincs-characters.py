###
# 28-12-2020
# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given a string s, and an integer k.
# Return the length of the longest substring in s that contains at most k distinct characters.

# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.
###

def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i

        if len(h) <= k:
            new_lower_bound = bounds[0]
        else:
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))