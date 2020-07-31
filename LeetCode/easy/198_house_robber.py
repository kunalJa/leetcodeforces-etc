"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    DP solution. First notice that since all houses provide positive value
    there never exists a time where we would skip more two houses at a time.
    Instead of skipping three houses we might as well also rob the hous in the middle.
    We keep track of the optimal robbed value of homes if you include robbing the current home.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)
        one_step = nums[1]
        two_steps = nums[0]
        three_steps = 0
        for i in range(2, len(nums)):
            optimal_at_i = nums[i] + max(two_steps, three_steps)
            three_steps, two_steps, one_step = two_steps, one_step, optimal_at_i
        return max(one_step, two_steps)
