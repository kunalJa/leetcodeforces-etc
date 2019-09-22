"""
https://codeforces.com/problemset/problem/977/D

Polycarp likes to play with numbers.
He takes some integer number x, writes it down on the board,
and then performs with it n−1 operations.
He either:
    divides the number x by 3 (if x is divisible by 3)
    multiplies the number x by 2

After each operation, Polycarp writes down the result on the board and replaces x
by the result. So there will be n numbers on the board after all.

Your problem is to rearrange (reorder) elements of this sequence in such a
way that it can match a possible Polycarp's game in the order of the numbers
written on the board.

I.e. each next number will be exactly two times of the previous number or exactly one
third of previous number.

A solution always exists.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Because we are told a solution will always exist, we learn a key fact:
        x, 2x and x/3 cannot all exist in the sequence

    Therefore, the list provided will always devolve into a chain, rather
    than any more complex directed graph (if you put an edge between x and 2x or x/3
    for all x in the input). The node with in-degree 0 is the starting node.
    Then, simply follow the edges of the graph.
"""
from sys import stdin, stdout


def rearrage_polycarp_math_and_sorting_solution(n: int, sequence):
    """
    Accepted
    Time Complexity: O(n log(n))
    Space Complexity: O(n)
    Solution Explanation:
        Sort the numbers based on exp(2, num) - exp(3, num).
        This is because in the sequence we are always either multiplying by 2
        i.e. increasing exp(2) by 1 or dividing by 3 i.e. decreasing exp(3) by 1.
        Further, we can simply sort by -exp(3) and then preserve smallest to largest
        for ties as 2x will always be larger than x.
    """

    def exp(b: int, a: int) -> int:
        """
        Returns the largest power of b that divides a.
        For example:
            exp(3, 27) returns 3 as b^3 | a and is the largest number to do so.
        """
        k = 0
        while a % b == 0:
            k += 1
            a //= b
        return k

    power_of_3 = [(-exp(3, num), num) for num in sequence]
    power_of_3.sort()

    return [num[1] for num in power_of_3]


def rearrage_polycarp(n: int, sequence):
    polys_seq = set(sequence)

    # Find the elements x of the sequence for which x/2 and 3x don't exist
    ordered_seq = [
        num
        for num in sequence
        if not (((num % 2 == 0) and (num // 2 in polys_seq)) or 3 * num in polys_seq)
    ]
    n -= 1
    i = 0
    while n:
        if 2 * ordered_seq[i] in polys_seq:
            ordered_seq.append(2 * ordered_seq[i])
        else:
            ordered_seq.append(ordered_seq[i] // 3)
        n -= 1
        i += 1

    return ordered_seq


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    sequence = [int(x) for x in stdin.readline().rstrip().split(" ")]
    stdout.write(
        " ".join(
            str(num) for num in rearrage_polycarp_math_and_sorting_solution(n, sequence)
        )
        + "\n"
    )
