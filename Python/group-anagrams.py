###
# 01-06-2021
# Hi, here's your problem today. This problem was recently asked by AirBNB:
#
# Given a list of words, group the words that are anagrams of each other.
# (An anagram are words made up of the same letters).
#
# Example:
#
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
###
import collections


def group_anagram_words(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1
        groups[tuple(char_count)].append(s)
    return list(groups.values())


print(group_anagram_words(['abc', 'bcd', 'cba', 'cbd', 'efg']))