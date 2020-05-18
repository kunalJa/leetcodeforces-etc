"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

Given a positive integer num, output its complement number.
The complement strategy is to flip the bits of its binary representation.
"""

"""
Accepted.
Time complexity: O(lg(n)), I feel like there is an O(1) solution since binary is so fundamental to computing.
Space complexity: O(1)
"""


class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join("1" if b == "0" else "0" for b in f"{num:b}"), 2)
