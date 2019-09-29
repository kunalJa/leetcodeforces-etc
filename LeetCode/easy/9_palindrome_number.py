"""
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Reverse the second half the number and compare it to the first half of the number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 2:
            return True

        # x can never have a 0 at the end because 010 will always be represented as 10.
        if x % 10 == 0:
            return False

        # Determine if x has odd or even length
        temp = x
        length = 0
        while temp > 0:
            temp //= 10
            length += 1

        reverse = 0
        while reverse < x:
            mod = x % 10
            reverse *= 10
            reverse += mod
            x //= 10

        if (
            length % 2 != 0
        ):  # If x is odd, then we need to add the center element back to x.
            x *= 10
            x += reverse % 10
        return reverse == x
