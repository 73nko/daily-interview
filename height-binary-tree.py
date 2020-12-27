###
# 27-12-2020
# Hi, here's your problem today. This problem was recently asked by Amazon:

# Given a binary tree, return all values given a certain height h.
###

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def values_at_height(root, height):
    if not root:
        return []
    if height == 1:
        return [root.value]

    left_node_values = values_at_height(root.left, height - 1)
    right_node_values = values_at_height(root.right, height - 1)

    return left_node_values + right_node_values


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(values_at_height(a, 3))