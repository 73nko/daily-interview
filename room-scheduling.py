###
# 08-01-2021
# Hi, here's your problem today. This problem was recently asked by Google:
#
# You are given an array of tuples (start, end) representing time intervals for lectures.
# The intervals may be overlapping. Return the number of rooms that are required.
###

def max_overlapping(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)

    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max


print(max_overlapping([(30, 75), (0, 50), (60, 150)]))