"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(1)
Solution Explanation:
    Using a slow pointer, we can keep track of the unique array built so far.
    We then continue iterating through the array swapping with the slow pointer
    each time we encounter a new element.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        unique = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[unique] = nums[i]
                unique += 1

        return unique

    def removeDuplicates_first_attempt(self, nums: List[int]) -> int:
        """
        Accepted
        Time complexity: O(n lg n) if the array needs to remain sorted, O(n) otherwise.
        Space complexity: O(1) once a wikisort is implemented.
        """
        n = len(nums)
        duplicates = 0
        prev = None
        for i in range(n - 1, -1, -1):
            if prev and nums[i] == nums[prev]:
                nums[prev], nums[n - 1 - duplicates] = (
                    nums[n - 1 - duplicates],
                    nums[prev],
                )
                duplicates += 1
            prev = i

        """
         At this point the array has no duplicates (within the range 0, n - duplicates), but has become unsorted.
         To remedy this, I would utilize a block sort.
         Some block sorts are inplace i.e O(1) space with O(n lg n) time complexity. For time constraints, I am avoiding implimenting that.
        """

        nums[0 : n - duplicates] = sorted(nums[0 : n - duplicates])
        # Again, I understand that this creates a temporary list of size n - duplicates and is therefore not O(1) space.

        return n - duplicates
