/*
 * Time Complexity : O(lg(n))
 * Space Complexity : the iterative solution is O(1), recursive is O(lg(n)) I believe
 * Algorithmic Paradigm : Divide and Conquer
 * 
 * 1) Calculate the medians m1 and m2 of the input arrays ar1[] 
 *     and ar2[] respectively.
 * 2) If m1 and m2 both are equal then we are done.
 *    return m1 (or m2)
 * 3) If m1 is greater than m2, then median is present in one 
 *    of the below two sub-arrays.
 *     a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
 *     b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
 * 4) If m2 is greater than m1, then median is present in one    
 *     of the below two sub-arrays.
 *     a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
 *     b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
 * 5) Repeat the above process until size of both the sub-arrays 
 *     becomes 2.
 * 6) If size of the two arrays is 2 then use below formula to get 
 *    the median.
 *    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
 */

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays of equal size.
 * You may assume nums1 and nums2 cannot be both empty.
 *  Example 1:
 *  Input: nums1 = [1, 3, 12] and nums2 = [2, 6, 13]
 *  Output: 4.5
 *  
 *  Example 2:
 *  Input: nums1 = [1, 2] and nums2 = [3, 4]
 *  Output: 2.5
 *  The median is (2 + 3)/2 = 2.5
 */

package LeetCode.medium;

public class Median_of_two_sorted_arrays_of_equal_length {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length == 0 && nums2.length == 0) return 0;
        return medianRecursiveHelper(nums1, nums2, 0, 0, nums1.length - 1, nums2.length - 1);
    }
    
    private static double medianRecursiveHelper(int[] nums1, int[] nums2,
            int start_1, int start_2, int end_1, int end_2) {

        int n1 = end_1 - start_1 + 1;
        int n2 = end_2 - start_2 + 1;
        if (n1 <= 2 && n2 <= 2)
            return (Math.max(nums1[start_1], nums2[start_2]) + Math.min(nums1[end_1], nums2[end_2])) / 2.0;
        double m1 = simpleMedian(nums1, start_1, end_1);
        double m2 = simpleMedian(nums2, start_2, end_2);
        
        if (m1 == m2)
            return m1;
        int len1 = n1 / 2;
        int len2 = n2 / 2;
        if (m1 < m2)
            return medianRecursiveHelper(nums1, nums2, start_1 + len1, start_2,
                    end_1, end_2 - len2);
        else
            return medianRecursiveHelper(nums1, nums2, start_1, start_2 + len2,
                    end_1 - len1, end_2);
    }
    
    private static double simpleMedian(int[] nums, int start, int end) {
        int medianPos = (end - start + 1)/2;
        if ((end - start + 1) % 2 != 0) {
            return nums[start + medianPos];
        } else {
            return (nums[start + medianPos - 1] + nums[start + medianPos]) / 2.0;
        }
    }
}