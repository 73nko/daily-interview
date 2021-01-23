###
# 20-01-2021
# Hi, here's your problem today. This problem was recently asked by Uber:
#
# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Note: be sure that pop() and top() handle being called on an empty stack.
###
class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.get_min(), x)))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def get_min(self):
        if self.stack:
            return self.stack[-1][1]
        return float("inf")


x = MinStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.get_min())
# -3
x.pop()
print(x.top())
# 0
print(x.get_min())