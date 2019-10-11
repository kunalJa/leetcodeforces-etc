"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Each time you find a value smaller than your latest max sell value, sell at your maximum sell
    and buy again at the value you are currently on.
    This is a greedy solution that takes advantage of the fact that if you have found a local
    maximum, it is more optimal to sell over waiting for an even higher srock price
    as it being a local maximum indicates that a value less than this maximum follows it
    meaning I can simply buy at that lower price and gain the net between the local max and the
    new buy price.

    Consider: [2,9,8,20]. My algorithm would produce (buy, sells) at (0, 1) and (2, 3) producing
    an overal gain of 19. If instead, at index 0 we waited until 20, we would only get a gain of
    18.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        commit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] < prices[sell - 1]:
                profit += commit
                commit = 0
                buy = sell

            commit = prices[sell] - prices[buy]

            sell += 1

        if commit > 0:
            profit += commit

        return profit
