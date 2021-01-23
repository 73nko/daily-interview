###
# 03-01-2021
# Hi, here's your problem today. This problem was recently asked by Twitter:
#
# You are given the root of a binary tree.
# Find and return the largest subtree of that tree, which is a valid binary search tree.
###
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def is_bst(root):
    def is_bst_helper(root, min_key, max_key):
        if root is None:
            return True
        if root.key <= min_key or root.key >= max_key:
            return False
        return is_bst_helper(root.left, min_key, root.key) and \
               is_bst_helper(root.right, root.key, max_key)

    return is_bst_helper(root, float('-inf'), float('inf'))


def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1


def largest_bst_subtree(root):
    def helper(root):
        # Returns a tuple of (size, root) of the largest subtree.
        if is_bst(root):
            return (size(root), root)
        return max(helper(root.left), helper(root.right), key=lambda x: x[0])

    return helper(root)[1]


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))