###
# 20-12-2020
# Hi, here's your problem today. This problem was recently asked by Uber:
#
# You have a landscape, in which puddles can form. You are given an array of non-negative
# integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

###
def capacity(arr):
    n = len(arr)
    left_maxes = [0 for _ in range(n)]
    right_maxes = [0 for _ in range(n)]

    current_left_max = 0
    for i in range(n):
        current_left_max = max(current_left_max, arr[i])
        left_maxes[i] = current_left_max

    current_right_max = 0
    for i in range(n - 1, -1, -1):
        current_right_max = max(current_right_max, arr[i])
        right_maxes[i] = current_right_max

    total = 0
    for i in range(n):
        total += min(left_maxes[i], right_maxes[i]) - arr[i]
    return total


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
