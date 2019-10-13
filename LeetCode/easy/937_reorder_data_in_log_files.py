"""
https://leetcode.com/problems/reorder-data-in-log-files/

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in
case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.
"""

"""
Accepted
Time Complexity: O(len(logs)^2 * len(logs[i]) as comparing two letter logs takes O(len(logs[i]))
Space Complexity: O(len(logs[i])) to swap two logs and to compare logs
Solution Explanation:
    Insertion Sort.
    The first log is considered sorted. Consider the next log.
    Swap the log left while it is "larger" than the previous log.
    A letter log is larger than all digit logs.
    Letter logs should be lexicographically sorted.

    You can optimize further by implementing a custom comparator for the object
    and use mergesort, or timsort or someother O(nlgn) algorithm.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        def is_smaller(log1: str, log2: str) -> str:
            """Returns true if log1 should appear before log2 in the final ordering."""
            nonlocal nums
            i = 0
            while i < len(log1) and log1[i] != " ":
                i += 1
            identifier_1 = i
            while i < len(log1) and log1[i] == " ":
                i += 1
            j = 0
            while j < len(log2) and log2[j] != " ":
                j += 1
            identifier_2 = j
            while j < len(log2) and log2[j] == " ":
                j += 1

            if log1[i] not in nums and log2[j] in nums:
                return True
            elif log1[i] not in nums and log2[j] not in nums:
                while i < len(log1) and j < len(log2):
                    if log1[i].lower() < log2[j].lower():
                        return True
                    elif log1[i].lower() > log2[j].lower():
                        return False

                    i += 1
                    j += 1
                    if (i < len(log1) and log1[i] != " ") and (
                        j >= len(log2) or log2[j] == " "
                    ):
                        return False
                    elif (j < len(log2) and log2[j] != " ") and (
                        i >= len(log2) or log1[i] == " "
                    ):
                        return True

                    while i < len(log1) and log1[i] == " ":
                        i += 1

                    while j < len(log2) and log2[j] == " ":
                        j += 1

                if i < len(log1) and j >= len(log2):
                    return True
                elif (
                    i >= len(log1)
                    and j >= len(log2)
                    and log1[:identifier_1] < log2[:identifier_2]
                ):
                    # The letters are all the same so we should compare identifiers
                    return True

            return False

        for i in range(1, len(logs)):
            current = logs[i]
            j = i - 1
            while j >= 0 and is_smaller(current, logs[j]):
                logs[j + 1] = logs[j]
                j -= 1
            logs[j + 1] = current

        return logs
