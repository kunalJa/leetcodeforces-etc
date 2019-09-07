class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        """Attempts to make sum(A) == sum(B) with one element swap from list A to list B.

        Returns:
            An integer list where the first element is the size of the candy bar Alice
            must swap and the second is the size of the candy bar Bob must swap.
            It is guaranteed that a solution exists.
        """
        '''
        # Brute Force -> try swapping every element until sum(A) == sum(B)
        # O(N^2 + M^2) since calculating sum is O(N)
        # O(NM) if we store the sum and simply manipulate the integer
        a_size = sum(A)
        b_size = sum(B)
        for i in range(len(A)):
            for j in range(len(B)):
                ij_swapped_a = a_size - A[i] + B[j]
                ij_swapped_b = b_size + A[i] - B[j]
                if ij_swapped_a == ij_swapped_b:
                    return [A[i], B[j]]
        '''
        alice = sorted(A)
        bob = sorted(B)
        print(alice)
        print(bob)
        a_sum = sum(alice)
        b_sum = sum(bob)
        print(a_sum)
        print(b_sum)
        sum_diff = a_sum - b_sum
        if 1 > 0:
            half_diff = sum_diff // 2
            i = 0
            j = 0
            while i < len(alice) and j < len(bob):
                swap_difference = alice[i] - bob[j]
                if swap_difference == half_diff:
                    return [alice[i], bob[j]]
                if alice[i] > bob[j]:
                    if swap_difference > half_diff: # Our difference needs to be smaller, so increment the smaller value to a larger value.
                        if swap_difference > 0:
                            j += 1
                        else:
                            i += 1
                    else:
                        if swap_difference > 0:
                            i += 1
                        else:
                            j += 1
                elif alice[i] < bob[j]:
                    if swap_difference > half_diff: # Our difference needs to be smaller, so increment the smaller value to a larger value.
                        if swap_difference < 0:
                            j += 1
                        else:
                            i += 1
                    else:
                        if swap_difference < 0:
                            i += 1
                        else:
                            j += 1
                else:
                    if half_diff > 0:
                        i += 1
                    else:
                        j += 1
