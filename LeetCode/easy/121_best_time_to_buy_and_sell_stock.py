"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(1)
Solution Explanation:
    Greedy, 2 Pointer solution.
    Each time we see a stock that is a higher price than the previous one,
    we update our max profit. If we see a stock lower than the price we bought
    at previously, we update our buy to purchase that stock. We can update the
    buy pointer without losing any information because it will always be the lowest price
    we have seen so far. So, if later there is a higher sell price, using this new buy pointer
    will always be better than if we used an older (and therefore higher) buy pointer.
"""


class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n < 2:
            return 0

        max_range = 0
        buy = 0
        for sell in range(0, n):
            if prices[sell] < prices[buy]:
                buy = sell

            if max_range < prices[sell] - prices[buy]:
                max_range = prices[sell] - prices[buy]

        return max_range

    def maxProfit_brute_force(self, prices) -> int:
        """
        Time Limit Exceeded
        Time Complexity: O(n^2)
        Space Complexity: O(1)
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
