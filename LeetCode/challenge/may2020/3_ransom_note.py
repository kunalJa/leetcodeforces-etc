"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

Given an arbitrary ransom note string and another string containing letters from all the
magazines, write a function that will return true if the ransom note can be constructed from the
magazines; otherwise, return false.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hist = defaultdict(int)
        for c in magazine:
            magazine_hist[c] += 1
        for c in ransomNote:
            magazine_hist[c] -= 1
            if magazine_hist[c] < 0:
                return False
        return True
