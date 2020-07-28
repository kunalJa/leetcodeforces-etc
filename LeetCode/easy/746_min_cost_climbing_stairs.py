'''
https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.
'''


'''
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    DP where we keep track of the min cost of reaching that step as the last step.
    The true last step cost would be the min of indexes -1 and -2, but we pretend while
    computing that the last step cost is just that of index -1.
    Then we get the recurrence: f[n] = min(f[n-1], f[n-2]) + cost[n]
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f, s = cost[0], cost[1]
        for i in range(2, len(cost)):
            newS = min(s, f) + cost[i]
            f, s = s, newS
        return min(f, s)
