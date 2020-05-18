"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊n/2⌋ times.

You may assume that the array is non-empty and the majority element always exist in the
array.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(1)
Solution:
    Single pass. Keep track of the most seen number so far (we've seen count "mode"s).
    If we have seen count numbers that are not mode, then we switch to a new mode.
    Takes advantage of the > n/2 constraint in the problem.
"""


class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        mode = nums[0]
        for num in nums:
            if count == 0:
                mode = num
            elif num != mode:
                count -= 2
            count += 1

        return mode
