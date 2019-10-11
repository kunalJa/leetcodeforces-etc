"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    First note that profit is defined by the difference in stock price at the buy and sell point.
    Thus, we build an array "diff" that computes the difference in stock price at each day.
    Consider finding the single best buy and sell point. This is the same problem as finding
    the maximum continuous subarray sum in the "diff" subarray. This led me to consider Kadane's
    algorithm.

    We precompute the maximum subarray from the left and from the right at each index.
    Then, comparing lsf[i] with rsf[i+1] is the same as comparing the maximum subarray
    in diff[:i] and diff[i:] (i.e. creating a partition of the "diff" array and providing us
    with the maximum profit if that partition is assumed).
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def kadane(arr: List[int], reversed: bool = False) -> List[int]:
            start = 0
            end = len(arr)
            step = 1
            if reversed:
                start = len(arr) - 1
                end = -1
                step = -1

            max_so_far = [0 for _ in range(len(arr))]
            count = 0
            for i in range(start, end, step):
                count += arr[i]

                if count < 0:
                    count = 0

                max_so_far[i] = max(max_so_far[i - step], count) if i != start else count

            return max_so_far

        diff = [prices[i] - prices[i-1] for i in range(1, len(prices)]
        if (len(diff) == 1):
            return max(0, diff[0])

        lsf = kadane()
        rsf = kadane(reversed = True)

        print(lsf)
        print(rsf)

        profit = 0
        for i in range(len(lsf) - 1):
            profit = max(profit, lsf[i] + rsf[i + 1])

        return profit
