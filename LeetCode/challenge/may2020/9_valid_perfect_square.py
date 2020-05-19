"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

Given a positive integer, write a function which returns True if num is a perfect square else False.

Do not use any built-in library function such as sqrt.
"""

"""
Accepted:
Time complexity: O(n) where n^2 is the input.
Space complexity: O(1)
Solution:
    The sum of the first x odd numbers = x^2.
    ex: {1 + 3 + 5 + 7 + 9 + 11 + 13 + 15} = 64 = 8^2
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        accumulator = 0
        i = 1
        while accumulator < num:
            accumulator += i
            i += 2
        return accumulator == num
