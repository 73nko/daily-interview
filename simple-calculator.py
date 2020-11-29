###
# 29-11-2020
# Hi, here's your problem today. This problem was recently asked by Google:

# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properationerly formed.

# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4
###

def evalHelp(expression, index=0):
    result = 0
    operation = '+'
    while index < len(expression):
        value = expression[index]
        if value.isdigit():
            if operation == '+':
                result += int(value)
            else:
                result -= int(value)
        elif value in ('+', '-'):
            operation = value
        elif value == '(':
            n, index = evalHelp(expression, index + 1)
            if operation == '+':
                result += n
            else:
                result -= n
        elif value == ')':
            return (result, index)
        index += 1
    return (result, index)


def eval(expression):
    return evalHelp(expression)[0]


print(eval('- (3 + ( 2 - 1 ) )'))
# -4
