###
# 08-01-2021
# Hi, here's your problem today. This problem was recently asked by Facebook:
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
###

def reverse_words(string):
    words = string.split(" ")
    reverse = ''
    for word in words:
        word = word[::-1]
        if reverse == '':
            reverse = word
        else:
            reverse = reverse + " " + word
    return reverse


print(reverse_words("The cat in the hat"))