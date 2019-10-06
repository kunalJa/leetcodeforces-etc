"""
https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of
five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def fizz(num: int) -> str:
            flag = False
            res = [str(num)]
            if num % 3 == 0:
                flag = True
                res.append("Fizz")
            if num % 5 == 0:
                flag = True
                res.append("Buzz")
            return "".join(res[1:]) if flag else "".join(res)

        return [fizz(i) for i in range(1, n + 1)]
