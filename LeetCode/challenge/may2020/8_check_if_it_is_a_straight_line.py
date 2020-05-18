"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

You are given an array coordinates [x,y].
Check if these points make a straight line in R2.
"""

"""
Accepted
Time complextiy: O(n)
Space complexity: O(1)
Solution:
    A set of collinear points have the same slope between them.
"""


class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) <= 2:
            return True
        x = 0
        y = 1
        Δx = coordinates[1][x] - coordinates[0][x]
        if Δx == 0:
            slope = float("inf")
        else:
            slope = (coordinates[1][y] - coordinates[0][y]) / Δx

        for i in range(2, len(coordinates)):
            Δx = coordinates[i][x] - coordinates[i-1][x]
            if Δx == 0:
                curr_slope = float("inf")
            else:
                curr_slope = (coordinates[i][y] - coordinates[i-1][y]) / Δx
            if curr_slope != slope:
                return False
        return True
