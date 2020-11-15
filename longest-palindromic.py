###
# 15-11-2020
# Daily Interview Pro
# Hi, here's your problem today. This problem was recently asked by Twitter:

# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.

# Example:
# Input: "banana"
# Output: "anana"

# Input: "million"
# Output: "illi"
###

class Solution:
    def longestPalindrome(self, s):
        s_leng = len(s)
        table = [[False for x in range(s_leng)] for y
                 in range(s_leng)]

        maxLength = 1
        i = 0

        while (i < s_leng):
            table[i][i] = True
            i = i + 1

        start = 0
        i = 0

        while i < s_leng - 1:
            if (s[i] == s[i + 1]):
                table[i][i + 1] = True
                start = i
                maxLength = 2
            i = i + 1

        k = 3

        while k <= s_leng:
            i = 0

            while i < (s_leng - k + 1):
                j = i + k - 1

                if (table[i + 1][j - 1] and
                        s[i] == s[j]):
                    table[i][j] = True

                    if (k > maxLength):
                        start = i
                        maxLength = k

                i = i + 1
            k = k + 1

        return s[start:start+maxLength]


# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
