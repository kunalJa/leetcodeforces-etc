"""
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Utilizing Gauss' formula we can figure out the expected sum versus the given sum.
    ∑i where i ranges from 0 to n (inclusive) equals n(n+1) / 2.
    The missing number is this expected value minus the actual sum of nums.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)

    def missingNumber_hashmap(self, nums: List[int]) -> int:
        """
        Accepted
        Time Complexity: O(n)
        Space Complexity: O(n)
        Solution Explanation:
            Create a hashable datastructure to be able to check the existence
            of an element in O(1) time. Then simply iterate over all number from 0 to n
            (inclusive) and check whether or not that number exists in the set.
        """
        map = set(nums)
        for i in range(len(nums) + 1):
            if i not in map:
                return i
