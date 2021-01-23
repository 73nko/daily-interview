###
# 27-11-2020
# Hi, here's your problem today. This problem was recently asked by LinkedIn:

# You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
###


def staircase2(n):
    response = [0 for x in range(n + 1)]
    response[0], response[1] = 1, 1

    for i in range(2, n + 1):
        j = 1
        while j <= 2 and j <= i:
            response[i] = response[i] + response[i-j]
            j = j + 1
    return response[n]


print(staircase2(5))
# 8
