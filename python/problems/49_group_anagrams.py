from collections import OrderedDict
from typing import List

"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters exactly
once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

"""
Time complexity = O(n * m * log(m))
Space complexity = O(n)
  n = # of given strings
  m = max length of any given string
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts: dict = dict()
        for i in range(len(strs)):
            count: tuple = tuple(self.count_chars(strs[i]).items())
            if count not in counts:
                counts[count] = []
            counts[count].append(strs[i])
        return list(counts.values())

    def count_chars(self, s: str) -> OrderedDict:
        count: dict = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] = count[s[i]] + 1
        return OrderedDict(sorted(count.items()))