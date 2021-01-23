###
# 15-11-2020
# Hi, here's your problem today. This problem was recently asked by Microsoft:
# Given a string, find the length of the longest substring without repeating characters.
# Here is an example solution in Python language. (Any language is OK to use in an interview,
# though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
###

class Solution:
    def lengthOfLongestSubstring(self, s):
        # create dictionary of letters and their latest index
        letters = {}
        # create a tail pointer, it updates whenever we meet a duplicate character
        tail = -1
        # create a head pointer, this one just iterates through every letter
        head = 0
        # result variable, updates whenever it's higher than result
        result = 0

        while head < len(s):
            if s[head] in letters:
                tail = max(tail, letters[s[head]])
            letters[s[head]] = head
            result = max(result, head-tail)
            head += 1
        return result


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijklmjxxx'))
# 13x
