"""
https://leetcode.com/problems/jewels-and-stones/

You're given strings J representing the types of stones that are jewels, and S representing
the stones you have. Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(n)
Solution Explanation:
    Create a map of possible characters in S to the number of their occurrences
    (i.e. A histogram made via a hashmap). Then iterate through each character in J
    and add up the number of times it appeared in the histogram to count.
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        hist = [0] * 59  # Using knowledge about ascii table
        for char in S:
            hist[ord(char) - 65] += 1
        for char in J:
            count += hist[ord(char) - 65]
        return count

    def numJewelsInStones_iterative(self, J: str, S: str) -> int:
        """
        Accepted
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        for char in S:
            if char in J:
                count += 1
        return count

    def numJewelsInStones_one_liner(self, J: str, S: str) -> int:
        """
        Accepted
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        return sum(1 for char in S if char in J)


"""
	The 'in' operator: e in L -> L.__containts__(e)
	https://wiki.python.org/moin/TimeComplexity
"""
