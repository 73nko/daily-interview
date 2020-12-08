#
# 08-12-2020
# Hi, here's your problem today. This problem was recently asked by Google:
# There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?
#
def witnesses(heights):
    witness_count = 0
    tall = 0
    for height in heights[::-1]:
        if height > tall:
            tall = height
            witness_count += 1

    return witness_count


print(witnesses([3, 6, 3, 4, 1]))
# 3
