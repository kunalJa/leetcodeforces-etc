"""
Accepted
Time complexity : O(n).
Space complexity : O(1).
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


class Solution:
    def maxProfit(prices) -> int:
        n = len(prices)
        if n < 2:
            return 0

        max_range = 0
        buy, sell = 0, 0
        for i in range(1, n):
            if prices[i] < prices[buy]:
                if max_range < prices[sell] - prices[buy]:
                    max_range = prices[sell] - prices[buy]
                buy, sell = i, i

            if prices[i] > prices[sell]:
                sell = i

        if max_range < prices[sell] - prices[buy]:
            max_range = prices[sell] - prices[buy]  # Include the final range found
        return max_range

    def maxProfit_brute_force(self, prices) -> int:
        """
        Time Limit Exceeded
        Time Complexity : O(n^2).
        Space Complexity : O(1).
        """
        n = len(prices)
        max_range = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > max_range:
                    max_range = prices[j] - prices[i]
        return max_range


if __name__ == "__main__":
    a = Solution
    print(a.maxProfit([1, 4, 2]))
