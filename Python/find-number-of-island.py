###
# 03-01-2021
# Hi, here's your problem today. This problem was recently asked by LinkedIn:
#
# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
# count the number of islands present in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.
###
def in_range(grid, r, c):
    num_row, num_col = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= num_row or c >= num_col:
        return False
    return True


def bfs(grid, curr_row, curr_col):
    queue = [(curr_row, curr_col)]
    # mark current vertex as visited
    grid[curr_row][curr_col] = 2
    while queue:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        curr_row, curr_col = queue.pop()
        for d in directions:
            next_row, next_col = curr_row + d[0], curr_col + d[1]
            if in_range(grid, next_row, next_col) and grid[next_row][next_col] == 1:
                queue.append((next_row, next_col))
                # mark next vertex and column as visited so
                # we don't double count
                grid[next_row][next_col] = 2


def num_islands_bfs(grid):
    if not grid or not grid[0]:
        return 0
    rows, columns = len(grid), len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                bfs(grid, i, j)
                count += 1
    return count


# Test Program
# Number of islands should be 3
grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(num_islands_bfs(grid))