"""
https://leetcode.com/problems/bag-of-tokens/

You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.
    If we have at least token[i] power, we may play the token face up, losing token[i] power,
    and gaining 1 point.
    If we have at least 1 point, we may play the token face down, gaining token[i] power,
    and losing 1 point.

Return the largest number of points we can have after playing any number of tokens.
"""

"""
Accepted
Time Complexity: O(n lgn) for sorting, algorithm part is O(n) O(1) space
Space Complexity: O(n) for sorting
Solution Explanation:
    I initially thought of the problem as knapsack, but on closer inspection an obvious pattern emerged- while you have power you should keep on gaining the most cost-effective points. Then when converting points to power you should only convert the most expensive items.
    Greedy: 2 pointer after sorting.
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        maxPoints = 0
        currPoints = 0
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if tokens[left] <= P:
                currPoints += 1
                P -= tokens[left]
                left +=1
            elif currPoints > 0:
                maxPoints = max(maxPoints, currPoints)
                P += tokens[right]
                currPoints -= 1
                right -= 1
            else:
                break
        maxPoints = max(maxPoints, currPoints)
        return maxPoints

    ''' testing in my head
    0 3 200 0
    1 3 100 1
    1 2 500 0
    2 2 300 1
    3 2 0 2
    '''
