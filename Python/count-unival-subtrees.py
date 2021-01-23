###
# 30-12-2020
# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# A unival tree is a tree where all the nodes have the same value.
# Given a binary tree, return the number of unival subtrees in the tree.
#
# For example, the following tree should return 5:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
#
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)
###

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival_subtrees(root):
    count, _ = count_unival_subtrees_helper(root)
    return count


def count_unival_subtrees_helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = count_unival_subtrees_helper(root.left)
    right_count, is_right_unival = count_unival_subtrees_helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.val != root.left.val:
            return total_count, False
        if root.right is not None and root.val != root.right.val:
            return total_count, False
        return total_count + 1, True
    return total_count, False


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5