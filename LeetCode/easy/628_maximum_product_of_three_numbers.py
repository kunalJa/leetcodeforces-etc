"""
https://leetcode.com/problems/maximum-product-of-three-numbers/

Given an integer array, find three numbers whose product is maximum and output the maximum
product.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
This solution was derived from the idea that the max can either be positive or negative.
Then let us consider the positive numbers and negative numbers in the array seperately.

if the max is a positive number:
	potential_max1 is the product of the 3 largest positive numbers or
	potential_max2 is the product of the 2 lowest negative numbers * the largest positive number

if the max is instead a negative number:
	potential_max3 is the product of the 3 highest negative numbers or
	potential_max4 is the product of the 2 lowest positive numbers * the highest negative number
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        second_smallest_pos, smallest_pos = 1001, 1001
        third_largest_pos, second_largest_pos, largest_pos = -1001, -1001, -1001

        third_largest_neg, second_largest_neg, largest_neg = -1001, -1001, -1001
        second_smallest_neg, smallest_neg = 1001, 1001

        for num in nums:
            if num >= 0:
                if num > largest_pos:
                    third_largest_pos = second_largest_pos
                    second_largest_pos = largest_pos
                    largest_pos = num
                elif num > second_largest_pos:
                    third_largest_pos = second_largest_pos
                    second_largest_pos = num
                elif num > third_largest_pos:
                    third_largest_pos = num

                if num < smallest_pos:
                    second_smallest_pos = smallest_pos
                    smallest_pos = num
                elif num < second_smallest_pos:
                    second_smallest_pos = num
            else:
                if num > largest_neg:
                    third_largest_neg = second_largest_neg
                    second_largest_neg = largest_neg
                    largest_neg = num
                elif num > second_largest_neg:
                    third_largest_neg = second_largest_neg
                    second_largest_neg = num
                elif num > third_largest_neg:
                    third_largest_neg = num

                if num < smallest_neg:
                    second_smallest_neg = smallest_neg
                    smallest_neg = num
                elif num < second_smallest_neg:
                    second_smallest_neg = num

        potential_max1 = (
            third_largest_pos * second_largest_pos * largest_pos
            if third_largest_pos != -1001
            else -float("inf")
        )
        potential_max2 = (
            third_largest_neg * second_largest_neg * largest_neg
            if third_largest_neg != -1001
            else -float("inf")
        )
        potential_max3 = (
            second_smallest_neg * smallest_neg * largest_pos
            if second_smallest_neg != 1001 and largest_pos != -1001
            else -float("inf")
        )
        potential_max4 = (
            second_smallest_pos * smallest_pos * largest_neg
            if second_smallest_pos != 1001 and largest_neg != -1001
            else -float("inf")
        )

        return max(potential_max1, potential_max2, potential_max3, potential_max4)
