"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Iterate through the array, if A[i] is negative, add its square to a negative list.
    If A[i] is positive, add it to a positive list.
    Merge the two sorted arrays.
"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squaredList = []
        pos = []
        neg = []

        for x in A:
            if x >= 0:
                pos.append(x ** 2)
            else:
                neg.append(x ** 2)

        pos_i = 0
        neg_i = len(neg) - 1
        while True:
            if pos_i >= len(pos):
                while neg_i >= 0:
                    squaredList.append(neg[neg_i])
                    neg_i -= 1
                break
            if neg_i < 0:
                while pos_i < len(pos):
                    squaredList.append(pos[pos_i])
                    pos_i += 1
                break
            if pos[pos_i] <= neg[neg_i]:
                squaredList.append(pos[pos_i])
                pos_i += 1
            else:
                squaredList.append(neg[neg_i])
                neg_i -= 1

        return squaredList
