"""
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses "(" and ")".
"""

"""
Accepted
Time complexity: O(2^n)
Space complexity: O(n)
Solution Explanation:
    Use a stack to figure out how many open parentheses errors and closed parentheses errors
    exist in the string. Then use recursion and backtracking to build valid solutions such that
    we have removed len(open_errors) "(" and len(closed_errors) ")"s.

    This solution prunes the number of solutions to check (and in fact doesn't validate that the
    expression built at the end of a recursion tree is valid as it is garunteed to be valid
    because we only add valid parentheses pairs to the expr and remove exactly the error
    number of invalid parentheses) as compared to a naiive backtracking solution.
    Both have the same worst case runtime though, despite this optimization.

"""
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open_errors = []
        closed_errors = []
        matching_parens = deque()
        for i in range(len(s)):
            if s[i] == "(":
                matching_parens.append(i)
            elif s[i] == ")":
                if matching_parens:
                    matching_parens.pop()
                else:
                    closed_errors.append(i)

        # Add all the leftover unclosed "("s to the list of invalid "("s
        for i in matching_parens:
            open_errors.append(i)

        newly_balanced_parentheses = set()

        def pruned_dfs(
            s: str,
            i: int,
            left_count: int,
            right_count: int,
            left_rem: int,
            right_rem: int,
            expr: List[str],
        ) -> None:

            if i >= len(s):  # The recursion reached the end of the string
                if (
                    left_rem == 0 and right_rem == 0
                ):  # We have removed the correct number of error "("s and error ")"s
                    newly_balanced_parentheses.add("".join(expr))

                return

            # Attempt to remove the current "(" or ")"
            if (s[i] == "(" and left_rem > 0) or (s[i] == ")" and right_rem > 0):
                pruned_dfs(
                    s,
                    i + 1,
                    left_count,
                    right_count,
                    left_rem - (s[i] == "("),
                    right_rem - (s[i] == ")"),
                    expr,
                )

            expr.append(s[i])

            if s[i] == "(":  # Include a "(" in the valid expression
                pruned_dfs(
                    s, i + 1, left_count + 1, right_count, left_rem, right_rem, expr
                )
            elif (
                s[i] == ")" and left_count > right_count
            ):  # Include a ")" in the valid expression
                pruned_dfs(
                    s, i + 1, left_count, right_count + 1, left_rem, right_rem, expr
                )
            elif (
                s[i] != "(" and s[i] != ")"
            ):  # Simply skip characters that are not "(" or ")"
                pruned_dfs(s, i + 1, left_count, right_count, left_rem, right_rem, expr)

            # Backtrack
            expr.pop()

        pruned_dfs(s, 0, 0, 0, len(open_errors), len(closed_errors), [])
        return list(newly_balanced_parentheses)
