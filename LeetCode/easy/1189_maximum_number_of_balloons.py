"""
https://leetcode.com/problems/maximum-number-of-balloons/

Given a string text, you want to use the characters of text to form as
many instances of the word "balloon" as possible.

You can use each character in text at most once.
Return the maximum number of instances that can be formed.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Create a histogram of the frequencies of the characters "b, "a",
    "l"," "o", and "n" in the input text.

    Try to reduce the frequency of all characters at once, if
    that is not possible, we can no longer create the word "balloon".
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {}
        balloon["b"] = 0
        balloon["a"] = 0
        balloon["l"] = 0
        balloon["o"] = 0
        balloon["n"] = 0
        for char in text:
            if not char in balloon:
                balloon[char] = 1
            else:
                balloon[char] += 1

        count = 0
        while (
            balloon["b"] > 0
            and balloon["a"] > 0
            and balloon["l"] > 1
            and balloon["o"] > 1
            and balloon["n"] > 0
        ):
            balloon["b"] -= 1
            balloon["a"] -= 1
            balloon["l"] -= 2
            balloon["o"] -= 2
            balloon["n"] -= 1
            count += 1

        return count
