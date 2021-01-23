###
# 26-11-2020
# Hi, here's your problem today. This problem was recently asked by Twitter:

# Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.
###
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, val):
        self.stack.append(val)
        if self.max:
            self.max.append(max(val, self.max[-1]))
        else:
            self.max.append(val)

    def pop(self):
        if self.max:
            self.max.pop()
        return self.stack.pop()

    def max(self):
        return self.max[-1]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
