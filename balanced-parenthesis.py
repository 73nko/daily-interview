###
# 16-11-2020
# # Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

# Example:
# Input: "((()))"
# Output: True

# Input: "[()]{}"
# Output: True

# Input: "({[)]"
# Output: False
###

openElements = ["[", "{", "("]
closeElements = ["]", "}", ")"]


class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c in openElements:
                stack.append(c)
            elif c in closeElements:
                if len(stack) <= 0:
                    return False
                # Compares the closing parenthesis to the
                # corresponding opening parenthesis using
                # their matching indices. We could also use
                # a hash map for this.
                if openElements.index(stack.pop()) != closeElements.index(c):
                    return False

        return len(stack) == 0


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))


s = "([{}])()"
print(Solution().isValid(s))
# should return True
