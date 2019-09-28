"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Using 2 pointers I iterate from both ends comparing each pair of characters
    that are alphanumeric.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanumeric(c: str) -> bool:
            return (
                ord("0") <= ord(c) <= ord("9")
                or ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
            )

        i = 0
        j = len(s) - 1
        while i <= j:
            if not alphanumeric(s[i]):
                i += 1
                continue

            if not alphanumeric(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
