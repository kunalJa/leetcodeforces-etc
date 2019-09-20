"""
https://leetcode.com/problems/fair-candy-swap/

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the
exchange, they both have the same total amount of candy.
(The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that
Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.
It is guaranteed an answer exists.
"""

"""
Accepted
Time complexity: O(n + m)
Space complexity: O(n + m) to store the sorted arrays, we could instead sort in place
Solution Explanation:
    We need to solve the equation: sum(A) - A[i] + B[j] == sum(B) - B[j] + A[i]
    i.e. sum(A) - sum(B) = 2A[i] - 2B[j]
    We simply iterate through A and B wisely, such that we can efficiently find the
    i and j that satisfies this equation.
"""


class Solution:
    def fairCandySwap_brute_force(self, A: List[int], B: List[int]) -> List[int]:
        """
        Time Limit Exceeded
        Time complexity: O(nm)
        Space complexity: O(1)
        Solution Explanation:
            Brute Force.
            We simply try swapping every element until sum(A) == sum(B).
        """
        a_size = sum(A)
        b_size = sum(B)
        for i in range(len(A)):
            for j in range(len(B)):
                ij_swapped_a = a_size - A[i] + B[j]
                ij_swapped_b = b_size + A[i] - B[j]
                if ij_swapped_a == ij_swapped_b:
                    return [A[i], B[j]]

    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        alice = sorted(A)
        bob = sorted(B)
        a_sum = sum(alice)
        b_sum = sum(bob)
        sum_diff = a_sum - b_sum
        half_diff = sum_diff // 2
        i = 0
        j = 0
        while i < len(alice) and j < len(bob):
            swap_difference = alice[i] - bob[j]
            if swap_difference == half_diff:
                return [alice[i], bob[j]]
            if alice[i] > bob[j]:
                if (
                    swap_difference > half_diff
                ):  # Our difference needs to be smaller, so increment the smaller value to a larger value.
                    if swap_difference > 0:
                        j += 1
                    else:
                        i += 1
                else:
                    if swap_difference > 0:
                        i += 1
                    else:
                        j += 1
            elif alice[i] < bob[j]:
                if (
                    swap_difference > half_diff
                ):  # Our difference needs to be smaller, so increment the smaller value to a larger value.
                    if swap_difference < 0:
                        j += 1
                    else:
                        i += 1
                else:
                    if swap_difference < 0:
                        i += 1
                    else:
                        j += 1
            else:
                if half_diff > 0:
                    i += 1
                else:
                    j += 1
