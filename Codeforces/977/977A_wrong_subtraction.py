"""
https://codeforces.com/problemset/problem/977/A

Little girl Tanya is learning how to decrease a number by one, but she does it wrong
with a number consisting of two or more digits. Tanya subtracts one from a number by the
following algorithm:
    if the last digit of the number is non-zero, she decreases the number by one;
    if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).

You are given an integer number n. Tanya will subtract one from it k times.
Your task is to print the result after all k subtractions.
"""

"""
Accepted
Time Complexity: O(n).
Space Complexity: O(1).
Solution Explantion: Apply tanya's subtraction algorithm to x y times.
"""
from sys import stdin, stdout


def tanya_subtract(x: int, y: int) -> int:
    """Tanya subtracts y from x"""
    tanya_result = x
    for i in range(y):
        if tanya_result % 10 == 0:
            tanya_result //= 10
        else:
            tanya_result -= 1
    return tanya_result


if __name__ == "__main__":
    x, y = map(int, stdin.readline().rstrip().split())
    stdout.write(str(tanya_subtract(x, y)) + "\n")
