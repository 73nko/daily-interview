###
# 04-12-2020
# Hi, here's your problem today. This problem was recently asked by Microsoft:
# You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

# Example:
# n = 2, m = 2

# This should return 2, since the only possible routes are:
# Right, down
# Down, right.
###
def num_ways(n, m):
    A = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        A[i][0] = 1
    for j in range(m):
        A[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[-1][-1]


print(num_ways(2, 2))
# 2
