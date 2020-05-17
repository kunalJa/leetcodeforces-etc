"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

You're given strings J representing the types of stones that are jewels, and S representing the
stones you have. Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.
"""

"""
Accepted
Time complexity: O(n)
Space comlexity: O(1)
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # This is a generator expression so no list is created in memory
        return sum(1 for char in S if char in J)
