"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Considering each element of the array, the maximum subarray sum is either the maximum
    ending at the previous element + the current element, or the current element by itself.
    In other words dp[i] = max(nums[i] + dp[i - 1], nums[i]).
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = None

        if nums:
            dp = nums[0]  # O(n) space factor optimization
            max_sub = nums[0]
            for i in range(1, len(nums)):
                dp = max(nums[i] + dp, nums[i])
                if dp > max_sub:
                    max_sub = dp

        return max_sub  # Constant factor time optimization

    def maxSubArray_not_optimized(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        if nums:
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                dp[i] = max(nums[i] + dp[i - 1], nums[i])

        return max(dp)

    def maxSubArray_divide_and_conquer(self, nums: List[int]) -> int:
        pass
