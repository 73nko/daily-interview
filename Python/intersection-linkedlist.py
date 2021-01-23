###
# 05-12-2020
# Hi, here's your problem today. This problem was recently asked by Apple:
# You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists are non-cyclical.

# Example:

# A = 1 -> 2 -> 3 -> 4
# B = 6 -> 3 -> 4

# This should return 3 (you may assume that any nodes with the same value are the same node).
###
def length(head):
    if not head:
        return 0
    return 1 + length(head.next)


def intersection(a, b):
    m, n = length(a), length(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in range(m - n):
            cur_a = cur_a.next
    else:
        for _ in range(n - m):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
