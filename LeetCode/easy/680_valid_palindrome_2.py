"""
https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Use two pointers to iterate from either end.
    If I see a discrepency in s[i] and s[j], then I consider ignoring s[i].
    If I still am not able to make a palindrome, I backtrack to the original discrepency
    and consider ignoring s[j] instead.
    If I am still unable to make a palindrome, return False.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag = False
        iteration = 1
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                if flag and iteration == 2:
                    return False
                elif flag:
                    # Consider ignoring s[j]
                    iteration = 2
                    i = fail_i
                    j = fail_j
                    j -= 1
                else:
                    # Consider ignoring s[i]
                    flag = True
                    fail_i = i
                    fail_j = j
                    i += 1
            else:
                i += 1
                j -= 1

        return True
