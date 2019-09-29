"""
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Modify the input in place.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Two pointer solution. A slow pointer called zero which keeps track of the first zero
    that needs to be replaced, and a faster pointer i which keeps track of the non-zero elements.
    We need only swap nums[i] and nums[zero] if zero < i and nums[i] != 0 but nums[zero] == 0.
    e.g. The algorithm will produce the following states after each swap.
        [1, 0, 0, 2, 12] (input)
        [1, 2, 0, 0, 12]
        [1, 2, 12, 0, 0]
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0 and nums[zero] == 0:
                nums[zero] = nums[i]
                nums[i] = 0

            if nums[zero] != 0:
                zero += 1
            i += 1
