"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Given a string S of lowercase letters, a duplicate removal consists of
choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed the answer is unique.
"""

"""
Accepted
Time Complexity: O(n^2)
Space Complexity: O(n)
Solution Explanation:
    2 pointer solution.
    Mark indices of duplicates in the string.
    Treat the string as not having those characters that are in marked indices.
    Move the lower index down until you reach an index that is not marked.
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        removed_indices = set()
        j = 0
        i = 1
        while i < len(S):
            if S[i] == S[j]:
                removed_indices.add(i)
                removed_indices.add(j)
                # Send j back to an index that has not yet been used in a pair
                while j in removed_indices:
                    j -= 1
                j -= 1

            j += 1
            if j in removed_indices:  # We have removed all indices left of i
                j = i
            elif j < 0:
                # If we removed the first pair, we need to increment both i and j
                i += 1
                j = i
            i += 1

        return "".join([S[i] for i in range(len(S)) if i not in removed_indices])

    def removeDuplicates_leetcode_solution(self, S: str) -> str:
        """
        Accepted
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        for c in S:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    def removeDuplicates_brute_force(self, S: str) -> str:
        """
        Time Limit Exceeded
        Time Complexity: O(n^2)
        Space Complexity: O(n) to make the new string S with each duplicate removed
        """
        i = 1
        while i < len(S):
            if S[i - 1] == s[i]:
                S = S[:i] + S[i + 1 :]
                i = 0
            i += 1
        return S
