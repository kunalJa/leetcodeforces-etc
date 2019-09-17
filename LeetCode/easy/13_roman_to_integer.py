"""
Accepted
Time complexity : O(n)
Space complexity : O(1)
"""

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        def romanChar(s: str) -> int:
            if s == "I":
                return 1
            elif s == "V":
                return 5
            elif s == "X":
                return 10
            elif s == "L":
                return 50
            elif s == "C":
                return 100
            elif s == "D":
                return 500
            elif s == "M":
                return 1000
            else:
                return 0

        total_val = 0
        i = 0
        while i < len(s):
            current_val = romanChar(s[i])
            if i + 1 < len(s):
                next_val = romanChar(s[i + 1])
                if current_val >= next_val:
                    total_val += current_val
                else:
                    total_val += next_val - current_val
                    i += 1
            else:
                total_val += current_val
            i += 1

        return total_val
