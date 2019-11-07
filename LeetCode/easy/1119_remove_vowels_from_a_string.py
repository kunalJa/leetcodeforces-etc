"""
https://leetcode.com/problems/remove-vowels-from-a-string/submissions/

Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}  # A set has O(1) lookup
        word = [c for c in S if c not in vowels]
        return "".join(word)
