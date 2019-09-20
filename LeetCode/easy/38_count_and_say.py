"""
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
"""

"""
Accepted
Time complexity: O(n * k) where k is the length of the longest string
Space complexity: O(n)
Solution Explanation:
    Brute force solution, iterative.
    Build the count and say sequence one at a time.
    To build each number in the sequence, simply iterate over the previous number
    keeping track of the number of repeated elements, appending this number to the current
    string before appending that number that was being repeated.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        current = ["1"]
        for i in range(1, n):
            current = []
            repeated = 1
            last_char = prev[0]
            for j in range(1, len(prev)):
                if prev[j] == last_char:
                    repeated += 1
                else:
                    current += str(repeated)
                    current += last_char
                    repeated = 1
                last_char = prev[j]
            current += str(repeated)
            current += last_char
            prev = "".join(current)

        return "".join(current)
