###
# 15-11-2020
# Hi, here's your problem today. This problem was recently asked by Microsoft:
# Given a string, find the length of the longest substring without repeating characters.
# Here is an example solution in Python language. (Any language is OK to use in an interview,
# though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
###

class Solution:
    def lengthOfLongestSubstring(self, s):
        result = 0
        count = 0
        stringBuffer = ''
        for c in s:
            if (stringBuffer.find(c) != -1):
                if result < count:
                    result = count
                count = 0
                stringBuffer = ''
            else:
                count += 1
                stringBuffer += c
        return result


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijklmjxxx'))
# 13x
