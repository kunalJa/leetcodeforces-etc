"""
https://leetcode.com/problems/subarray-product-less-than-k/

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the
subarray is less than k.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    2 pointer solution.
    Each time the product is less than k, increment the right pointer.
    If the product is greater than k, increment the left pointer.
    Finally, we add the number of subarrays that are less than k each time
    we successfully increment the right pointer to count.
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        left = 0
        right = 0
        count = 0
        pi = 1
        while right < len(nums):
            pi *= nums[right]
            if pi < k:
                count += right - left + 1
                right += 1
            elif left == right:
                pi = 1
                left += 1
                right += 1
            else:
                pi //= nums[left]
                pi //= nums[right]
                left += 1

        return count
