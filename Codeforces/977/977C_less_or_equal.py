"""
https://codeforces.com/problemset/problem/977/C

You are given a sequence of integers of length n and integer number k.
You should print any integer number x in the range of [1;10^9] (i.e. 1≤x≤10^9)
such that exactly k elements of given sequence are less than or equal to x.
"""

"""
Accepted
Time Complexity: O(nlogn)
Space Complexity: O(1)
Solution Explanation:
    Sort the sequence and find the kth largest number.
    Iterate over the array to ensure that this number is not bloated by duplicates.
"""
from sys import stdin, stdout

# from random import randrange


def kth_largest_integer(k: int, sequence) -> int:
    sequence.sort()
    if k == 0:
        kth = sequence[0] - 1
    else:
        kth = sequence[k - 1]

    count = 0
    for num in sequence:
        if num <= kth:
            count += 1

    if count == k and kth > 0:
        return kth

    return -1


def kth_largest_integer_no_duplicates(k: int, sequence) -> int:
    """
    Solution Explantion :
        Using an algorithm based off of quick sort, we are partitioning the array several times
        to try and select the kth largest integer in the array. When partitioning, we use a
        unique algorithm to ensure that the partition can happen in O(end - start) time via
        swapping larger elements to the end of the array and moving the partiotion forward when
        considering smaller elements.

    Unfortunately, I couldn't get this solution to account for duplicates any faster than O(nlogn) so I abandoned it for now.
    """
    start = 0
    end = len(sequence) - 1
    pivot = __random_partition_in_place(start, end, sequence)
    while start <= end:
        if k == pivot + 1:
            return sequence[pivot]
        elif k < pivot + 1:
            end = pivot - 1
            pivot = __random_partition_in_place(start, end, sequence)
        else:
            start = pivot + 1
            pivot = __random_partition_in_place(start, end, sequence)

    return -1


def __random_partition_in_place(start: int, end: int, sequence) -> int:
    """
    Partitions the subarray (start, end inclusive) such that all elements to the left of the pivot are <= the pivot and all elements to the right of the pivot are > than the pivot.
    Returns the final index of the pivot element.
    """
    pivot = randrange(start, end, 1)
    sequence[start], sequence[pivot] = sequence[pivot], sequence[start]
    pivot = start
    start += 1
    while start <= end:
        # If the next element is smaller than our pivot element, swap them
        if sequence[start] <= sequence[pivot]:
            sequence[start], sequence[pivot] = sequence[pivot], sequence[start]
            pivot += 1
            start += 1
        # If the next element is larger than our pivot element, swap it with the last unsorted element
        else:
            sequence[start], sequence[end] = sequence[end], sequence[start]
            end -= 1

    return pivot


if __name__ == "__main__":
    n, k = map(int, stdin.readline().rstrip().split(" "))
    sequence = [int(x) for x in stdin.readline().rstrip().split(" ")]
    stdout.write(str(kth_largest_integer(k, sequence)) + "\n")
