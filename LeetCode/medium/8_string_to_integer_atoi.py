"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes an optional initial
plus or minus sign followed by as many numerical digits as possible, and interprets them as a
numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit
    signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of
    representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
"""

"""
Accepted
Time Complexity: O(n)
Space Coplexity: O(1)
Solution Explanation:
    Simply iterate through the string checking for the conditions given in the problem.
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        dictionary = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        sign = 1
        ret = 0
        i = 0
        while i < len(s) and s[i] is " ":
            i += 1

        if i < len(s) and s[i] is "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] is "+":
            i += 1

        while i < len(s) and s[i] in dictionary:
            if (
                ret * 10 + dictionary[s[i]] < ret
                or ret * 10 + dictionary[s[i]] > 2 ** 31 - 1
            ):
                if sign == -1:
                    return -(2 ** 31)
                else:
                    return 2 ** 31 - 1
            ret *= 10
            ret += dictionary[s[i]]
            i += 1

        return ret * sign
