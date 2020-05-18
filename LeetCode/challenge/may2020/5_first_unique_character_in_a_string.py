"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        histogram = defaultdict(int)
        for c in s:
            histogram[c] += 1
        for i, c in enumerate(s):
            if histogram[c] == 1:
                return i
        return -1
