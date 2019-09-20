"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

Given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.
Parantheses will always be balanced if they exist.
"""

"""
Accepted
Time Complexity : O(n^2)
Space Complexity : O(n)
Solution Explanation:
    Find the first ")", keeping track of the last "(" we've seen.
    Reverse the characters between theese parentheses.
    Update the position of "visited" / already used parentheses while reversing.
    (i.e. "(a())" -> "(()a)" causes the used parentheses go from index 2 to 1).
    Now continually devrement the "(" pointer to find the previous open paren.

    Increment the pointer looking for ")" and repeat.
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        char_array = [c for c in s]
        seen = {i: False for i in range(len(char_array))}

        def reverseSubarray(start: int, end: int) -> None:
            nonlocal char_array
            nonlocal seen

            for i in range((end - start) // 2 + 1):
                char_array[start + i], char_array[end - i] = (
                    char_array[end - i],
                    char_array[start + i],
                )

                # Swap parentheses to their opposite as we only care about reversing chars
                if char_array[start + i] == "(":
                    char_array[start + i] = ")"
                elif char_array[start + i] == ")":
                    char_array[start + i] = "("
                if start + i != end - i and char_array[end - i] == "(":
                    char_array[end - i] = ")"
                elif start + i != end - i and char_array[end - i] == ")":
                    char_array[end - i] = "("

                # Update the position of already used "("
                if char_array[start + i] == "(":
                    seen[start + i] = True
                if char_array[end - i] == "(":
                    seen[end - i] = True
                if char_array[start + i] == ")":
                    seen[start + i] = False
                if char_array[end - i] == ")":
                    seen[end - i] = False

        open_paren = 0
        closed_paren = 0
        while closed_paren < len(char_array):
            if char_array[closed_paren] == "(":
                open_paren = closed_paren
            elif char_array[closed_paren] == ")":
                reverseSubarray(open_paren, closed_paren)
                while open_paren >= 0 and (
                    char_array[open_paren] != "("
                    or (char_array[open_paren] == "(" and seen[open_paren])
                ):
                    open_paren -= 1
            closed_paren += 1

        char_array_without_parentheses = [
            c for c in char_array if c != "(" and c != ")"
        ]
        return "".join(char_array_without_parentheses)
