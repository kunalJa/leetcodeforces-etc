"""
https://leetcode.com/problems/rotated-digits/

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?
"""

"""
Accepted
Time complexity: O(n * log(n)) because log10(n) tells us how many digits the number has
Space complexity: O(1)
Solution Explanation:
    Iterate from 1 to N and for each number check each digit and see if it is made up entirely
    of good numbers.
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:

        goodMapping = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}
        goodNums = 0

        for i in range(1, N + 1):
            badNum = False
            original = i
            rotated = 0
            placeValue = 0

            while i > 0:
                try:
                    rotated += goodMapping.get(i % 10) * (10 ** placeValue)
                except:
                    badNum = True
                    break
                placeValue += 1
                i = i // 10

            if not badNum and original != rotated:
                goodNums += 1

        return goodNums
