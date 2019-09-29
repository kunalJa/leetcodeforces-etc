"""
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas.
There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.
Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
If the pile has less than K bananas, she eats all of them instead, and won't eat any more
bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the
guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.
"""

"""
Accepted
Time Complexity: O(lg(max(piles)) * n)
Space Complexity: O(1)
Solution Explanation:
    Binary search for the mimum number of bananas Koko can eat per hour.
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def can_eat_all_within_H(piles: List[int], k: int, H: int):
            time_to_eat_all = 0
            for bananas in piles:
                time_to_eat_all += bananas // k
                if bananas % k > 0:
                    time_to_eat_all += 1

            return time_to_eat_all <= H

        left = 1
        right = max(piles)
        # The worst case scenario is the max number that koko can eat bananas
        min_hours = right
        while left < right:
            middle = left + (right - left) // 2
            if can_eat_all_within_H(piles, middle, H):
                right = middle
                min_hours = middle
            else:
                left = middle + 1

        return min_hours
