###
# 16-01-2021
# Hi, here's your problem today. This problem was recently asked by Apple:
#
# You are given a binary tree representation of an arithmetic expression.
# In this tree, each leaf is an integer value, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
#
# Write a function that takes this tree and evaluates the expression.
#
# Example:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
# This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.
###

###
# Solution
# The solution to this problem is a simple recursive approach. For a given node,
# if it is an operation, we recursively evaluate the left and right subtree,
# apply the operator on the results, and return that value. Otherwise,
# if the value is an integer, we simply return that integer.
###
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def evaluate(root):
    if root.val == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    elif root.val == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    elif root.val == TIMES:
        return evaluate(root.left) * evaluate(root.right)
    elif root.val == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))