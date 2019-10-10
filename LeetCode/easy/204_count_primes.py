"""
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.
"""

"""
Accepted
Time Complexity: O(n^1.5)
Space Complexity: O(n)
Solution Explanaton:
    In mathematics, the Sieve of Eratosthenes is an ancient algorithm for finding all prime
    numbers up to any given limit. It does so by iteratively marking as composite (i.e., not
    prime) the multiples of each prime, starting with the first prime number, 2.
    The multiples of a given prime are generated as a sequence of numbers starting from that
    prime, with constant difference between them that is equal to that prime.
"""


class Solution:
    def countPrimes_sieve_of_eratosthenes(self, n: int) -> int:
        if n < 2:
            return 0

        marked = set()
        seive = [i for i in range(1, n)]
        skip = 2
        while skip * skip < n:
            if skip not in marked:
                marked.update(seive[2 * skip - 1 :: skip])
            skip += 1

        return len(seive) - len(marked) - 1
