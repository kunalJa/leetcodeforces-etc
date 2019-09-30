"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Create an array that accumulates value overtime.
    This is the sum of the subarray starting at 0 and ending at i.
    Then consider given the current accumulation, have we seen previously a value
    accumulation - k? If so, then we have found a subarray that sums to k:
        accumulation - (accumulation - k) = k.
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        accumulator = 0
        seen = {0: 1}
        for num in nums:
            accumulator += num
            if accumulator - k in seen:
                count += seen[accumulator - k]
            if accumulator not in seen:
                seen[accumulator] = 0
            seen[accumulator] += 1
        return count

    def subarraySum_hash_of_hash(self, nums: List[int], k: int) -> int:
        """
        Memory Limit Exceeded
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        Solution explanation:
            I was close with this solution.
            I had to make a hashmap of hashmaps because I needed to ensure that
            the accumulation I was looking for existed after the current element.
            If I had realized that I was considering the accumulation that started at i
            rather than ended at i, I could have avoided another hashmap and instead
            iterated in reverse.
        """
        accumulative_count = {i: {} for i in range(len(nums))}
        accumulative_list = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            accumulative_list[i] = nums[i]
            if i > 0:
                accumulative_list[i] += accumulative_list[i - 1]

            if accumulative_list[i] not in accumulative_count[0]:
                accumulative_count[0][accumulative_list[i]] = 0

            accumulative_count[0][accumulative_list[i]] += 1

        for i in range(1, len(accumulative_list)):
            accumulative_count[i] = accumulative_count[i - 1].copy()
            accumulative_count[i][accumulative_list[i - 1]] -= 1

        count_subarrays = 0
        for i in range(len(accumulative_list)):
            target = k
            if i != 0:
                target += accumulative_list[i - 1]

            if target in accumulative_count[i]:
                # Somehow I need to make sure I only look for those that come after i
                count_subarrays += accumulative_count[i][target]

        return count_subarrays

    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        """
        Time Limit Exceeded (Though it would pass in Java or C++)
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(len(nums)):
            subarray = 0
            for j in range(i, len(nums)):
                subarray += nums[j]
                if subarray == k:
                    count += 1

        return count
