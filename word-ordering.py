###
# 02-12-2021
# Hi, here's your problem today. This problem was recently asked by Apple:
#
# Given a list of words, and an arbitrary alphabetical order,
# verify that the words are in order of the alphabetical order.
#
# Example:
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: False
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'
#
# Example 2:
# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: True
# Explanation: The words are in increasing alphabetical order
###

def is_sorted(words, order):
    order_mapping = {char: idx for idx, char in enumerate(order)}
    if len(words) <= 1:
        return True

    last_word = [order_mapping[c] for c in words[0]]

    for word in words[1:]:
        new_word = [order_mapping[c] for c in word]
        if last_word > new_word:
            return False
        last_word = new_word
    return True


print(is_sorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(is_sorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))