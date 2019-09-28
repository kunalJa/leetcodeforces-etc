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
from typing import List


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
        def d_c(start: int, exclusive_end: int) -> [int, int, int]:
            """
            @returns the range of the maximum subarray and also its value
            (i, j, max)
            """
            if start + 1 >= exclusive_end:  # Subarray of len 1
                return [start, exclusive_end, nums[start]]

            mid = start + (exclusive_end - start) // 2
            left = d_c(start, mid)
            right = d_c(mid, exclusive_end)

            center_from_l = [left[0], left[1], left[2]]
            left_sum = left[2]
            i = left[1]
            while i < right[1]:
                left_sum += nums[i]
                if center_from_l[2] < left_sum:
                    center_from_l[1] = i
                    center_from_l[2] = left_sum

                i += 1

            center_from_r = [right[0], right[1], right[2]]
            right_sum = right[2]
            i = right[0] - 1
            while i >= left[0]:
                right_sum += nums[i]
                if center_from_r[2] < right_sum:
                    center_from_r[0] = i
                    center_from_r[2] = right_sum

                i -= 1

            return max([center_from_l, center_from_r], key=lambda x: x[2])

        if not nums:
            return -1

        return d_c(0, len(nums))[2]
