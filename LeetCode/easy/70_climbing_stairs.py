"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    I am assuming (1, 2) is different from (2, 1).
    We calculate in reverse from the brute force solution (i.e. we consider distance 0 to n
    first and then distance 1 to n and then distance 2 to n, etc.)
    We already know that distance 0 to end has only 1 solution.
    Similarly, distance 1 to end has only 1 solution.
    At that point, we know that the solution is based on the sum of the previous 2 solutions:
        dp[i] = dp[i-1] + dp[i+1]
"""

# [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs_brute_force(self, n: int) -> int:
        def recurse(i, n):
            if i == n:
                return 1
            if i > n:
                return 0

            return recurse(i + 1) + recurse(i + 2)

        return recurse(0, n)
