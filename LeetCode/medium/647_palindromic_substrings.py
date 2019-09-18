"""
Accepted
Time complexity : O(n)
Space complexity : O(n)
Solution explanation : A substring s[i:j] is a palindrome if s[i] == s[j] and s[i+1:j-1]
is a palindrome.
"""

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def outward_palindrome(i: int, j: int) -> int:
            nonlocal s

            count = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    count += 1
                    i -= 1
                    j += 1
                else:
                    break
            return count

        count = 0
        for i in range(len(s)):
            count += outward_palindrome(i, i)
            count += outware_palindrom(i, i + 1)

        return count
