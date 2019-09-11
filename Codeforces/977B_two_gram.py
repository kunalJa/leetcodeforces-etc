"""
https://codeforces.com/problemset/problem/977/B

Two-gram is an ordered pair (i.e. string of length two) of capital Latin letters. For example, "AZ", "AA", "ZA" — three distinct two-grams.

You are given a string s
consisting of n capital Latin letters. Your task is to find any two-gram contained in the given string as a substring (i.e. two consecutive characters of the string) maximal number of times. For example, for string s = "BBAABBBA" the answer is two-gram "BB", which contained in s three times. In other words, find any most frequent two-gram.
"""

"""
Accepted
Time Complexity : O(n).
Space Complexity : O(1).
Solution Explantion : For every substring s of length 2, iterate over the latin string and count how many occurrences it has. Keep track of the substring s with the largest mode.
"""
from sys import stdin, stdout


def mode_two_gram_SpaceOptimized(n: int, latin: str) -> str:
    """This solution requires O(n^2) time to run but O(1) space"""
    max_occurrenes = 0
    for i in range(n - 1):
        count = 0
        two_gram = latin[i] + latin[i + 1]
        # counting the occurences of the two_gram in the string
        for j in range(n - 1):
            if two_gram == latin[j] + latin[j + 1]:
                count += 1

        if max_occurrenes < count:
            max_occurrenes = count
            max_two_gram = two_gram

    return max_two_gram


def mode_two_gram_TimeOptimized(n: int, latin: str) -> str:
    """This solution requires O(n) time to run but O(n) space for the histogram"""
    histogram = {}
    for i in range(n - 1):
        two_gram = latin[i] + latin[i + 1]
        if not two_gram in histogram:
            histogram[two_gram] = 1
        else:
            histogram[two_gram] += 1

    return max(histogram, key=lambda k: histogram[k])


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    latin = stdin.readline().rstrip()
    stdout.write(mode_two_gram_SpaceOptimized(n, latin) + "\n")
