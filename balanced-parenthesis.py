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
        open = []
        for i in s:
            if i in openElements:
                open.append(i)
            elif i in closeElements:
                pos = closeElements.index(i)
                if ((len(open) > 0) and (openElements[pos] == open[len(open)-1])):
                    open.pop()
                else:
                    return False

        if len(open) == 0:
            return True
        else:
            return False


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
