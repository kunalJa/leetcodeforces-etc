"""
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater
permutation of numbers.

If such arrangement is not possible, it must rearrange it as the
lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.
For example:
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Search throught the list in reverse.
    Find the first occurance of a number that is larger than the number previous to it.
    (i.e. look for nums[i] > nums[i - 1])
    This number is the number we need to change in order to get to the next permutation.
    Clearly all the numbers until nums[i] (from the end) are in ascending order.
    Then we need only reverse this list to ensure that the number is the next smallest number.
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse_in_place_from(start: int) -> None:
            nonlocal nums
            i = start
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        start = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i
                while j < len(nums) and nums[j] > nums[i - 1]:
                    j += 1

                # We want to swap with the smallest number larger than nums[i - 1]
                j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                start = i
                break

        # If we did not yet return, then we must instead return the smallest permutation
        # We can do this simply by reversing the list
        reverse_in_place_from(start)
