class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subset_of_sum(Z, A) -> bool:
            # Create the memo table of dimension Z by n
            n = len(A)
            memo = [[None for _ in range(n + 1)] for _ in range(Z + 1)]

            for i in range(n+1): # Having found a subset that reaches the sum
                memo[0][i] = True

            for i in range(Z+1): # Having run out of array elements without reaching the sum
                memo[i][n] = False

            # i implies the subarray A[i:]
            def rec_subset_of_sum(Z, i):
                if Z < 0:
                    return False
                if memo[Z][i] is None:
                    memo[Z][i] = rec_subset_of_sum(Z, i + 1) or rec_subset_of_sum(Z - A[i], i + 1)
                return memo[Z][i]

            return rec_subset_of_sum(Z, 0)
        
        Z = sum(nums)
        if Z % 2 == 0:
            return subset_of_sum(Z//2, nums)
        return False