"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine
the maximum amount of money you can rob tonight without alerting the police.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    DP, this is the same as house robber 1. A circular street design just means that if we
    chose the first house we cannot choose the last home. If we choose the last home,
    we cannot choose the first. We can then just use the solution to house robber 1
    twice- once for [0:-1] and another for [1:].
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums, default=0)
        def rob_street(start: int, end: int) -> int:
            one_step = nums[start + 1]
            two_steps = nums[start]
            three_steps = 0
            for i in range(start + 2, end):
                optimal_at_i = nums[i] + max(two_steps, three_steps)
                three_steps, two_steps, one_step = two_steps, one_step, optimal_at_i
            return max(one_step, two_steps)
        return max(rob_street(0, n - 1), rob_street(1, n))
