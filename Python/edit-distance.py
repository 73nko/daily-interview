###
# 28-11-2020
# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given two strings, determine the edit distance between them. The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).
###

def distance(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    return min(distance(s1[1:], s2) + 1,
               distance(s1, s2[1:]) + 1,
               distance(s1[1:], s2[1:]) if s1[0] == s2[0]
               else distance(s1[1:], s2[1:]) + 1)


print(distance('biting', 'sitting'))
# 2
