"""
https://leetcode.com/problems/longest-palindrome/

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Create a histogram of letters in the string.
    A palindrome can have infinite pairs of characters but only 1 single character.
    Simply count the number of characters of which you can use an even number.
    Add 1 if there exists an odd numbered count.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        histogram = {}
        for c in s:
            if c not in histogram:
                histogram[c] = 0
            histogram[c] += 1

        solo_char_used = False
        max_len = 0
        for count in histogram.values():
            if count % 2 == 0:
                max_len += count
            else:
                solo_char_used = True
                max_len += count - 1

        if solo_char_used:
            max_len += 1
        return max_len
