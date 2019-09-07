/**
 * The first thing to do is convert the problem into a more basic question--
 * Finding the k-th smallest element in two sorted arrays.
 * So the original question became finding the (n+m+1)/2 th element if n+m is odd
 * and finding both (n+m)/2 and (n+m+2)/2 th elements if n+m is even.
 */

/*
 * Couldn't figure out -> had to look at solution.
 * Time Complexity : O(lg(Min(m,n))
 * Space Complexity : O(1); 
 * See medium for median of two sorted arrays of the same size.
 * A key difference in this solution is what to do in the case of
 * A = [4, 7, 9]
 * B = [5]
 * You can't just eliminate 9, and not 4 before going to the next iteration.
 * Doing so will result in a median of 5 instead of the true median of 6.
 * An easy solution might be to compare the number from the single list (5)
 * against the first and last elements in the list and remove the highest and lowest numbers.
 * This works, but this takes n/2 operations, resulting a time complexity O(n).
 */

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays.
 * The overall run time complexity should be O(log (m+n)).
 * You may assume nums1 and nums2 cannot be both empty.
 *  Example 1:
 *  Input: nums1 = [1, 3] and nums2 = [2]
 *  Output: 2.0
 *  
 *  Example 2:
 *  Input: nums1 = [1, 2] and nums2 = [3, 4]
 *  Output: 2.5
 *  The median is (2 + 3)/2 = 2.5
 */

package LeetCode.hard;

public class Median_of_two_sorted_arrays {
    public static double findMedianSortedArrays(int[] input1, int[] input2) {
        /**
         * There are two sorted arrays nums1 and nums2 of size m and n respectively.
         *
         * Solution
         * Take minimum size of two array. Possible number of partitions are from
         * 0 to m in m size array. Try every splitting of the two arrays through
         * binary search. When you cut first array at i then you cut second array
         * at (m + n + 1)/2 - i. This is because at the median splitting, there are equal
         * sized sub arrays on both the left partition and the right partition 
         * (or + 1 on left if odd length). Now try to find the i where
         * a[i-1] <= b[j] and b[j-1] <= a[i], this again is necessary to be the median.
         */
        //if input1 length is greater than switch them so that input1 is smaller than input2.
        if (input1.length > input2.length) {
            int[] temp = input1;
            input1 = input2;
            input2 = temp;
            //return findMedianSortedArrays(input2, input1);
        }
        
        int x = input1.length;
        int y = input2.length;

        int low = 0;
        int high = x;
        while (low <= high) {
            int partitionX = (low + high)/2;
            int partitionY = (x + y + 1)/2 - partitionX;

            //if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            //if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : input1[partitionX - 1];
            int minRightX = (partitionX == x) ? Integer.MAX_VALUE : input1[partitionX];

            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : input2[partitionY - 1];
            int minRightY = (partitionY == y) ? Integer.MAX_VALUE : input2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                //We have partitioned array at correct place
                // Now get max of left elements and min of right elements to get the median in case of even length combined array size
                // or get max of left for odd length combined array size.
                if ((x + y) % 2 == 0) {
                    return ((double)Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY))/2;
                } else {
                    return (double)Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) { //we are too far on right side for partitionX. Go on left side.
                high = partitionX - 1;
            } else { //we are too far on left side for partitionX. Go on right side.
                low = partitionX + 1;
            }
        }

        //Only we we can come here is if input arrays were not sorted. Throw in that scenario.
        throw new IllegalArgumentException();
    }
}

/*
 * Below is a bad brute force solution that is O(n + m) in both space and time complexity.
 * 
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length, len2 = nums2.length;
        int l1 = 0, l2 = 0, i = 0;
        int[] merge = new int[len1 + len2];
        while (l1 < len1 || l2 < len2) {
            if (l1 > len1 && l2 < len2) {
                merge[i++] = nums1[l1++];
            } else if (l2 > len2 && l1 < len1) {
                merge[i++] = nums2[l2++];
            } else {
                if (nums1[l1] <= nums2[l2]) {
                    merge[i++] = nums1[l1++];
                } else {
                    merge[i++] = nums2[l2++];
                }
            }
        }
        
        if (merge.length % 2 == 0) {
            return (double) (merge[(merge.length - 1) / 2] + merge[merge.length / 2]) / 2.0;
        }
        return merge[merge.length / 2]; 
    }
 */

/*
 * Another brute force solution that has O (n + m) time complexity, but only O(1) space.
 * This solution can probably be improved as far as the implementation goes.
 * The algorithm is to find the indices on both num1 and num2 where we have gone through
 * n/2 spots (the median location). There is then a bunch of different scenarios to take into
 * account like both arrays are of size 1 or both the middle numbers (in an even length array)
 * are in one array and not the other.
 * 
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length + nums2.length;
        int med = n / 2;
        if (n % 2 == 0) {
            int i = 0, j = 0;
            while (n > med - 1) {
                if (i < nums1.length && j < nums2.length) {
                    if (nums1[i] <= nums2[j]) ++i;
                    else ++j;
                } else if (i >= nums1.length && j < nums2.length) {
                    ++j;
                } else {
                    ++i;
                }
                --n;
            }
            if (i > 1 && j > 1) {
                if (nums1[i - 1] > nums2[j - 1]) {
                    if (nums1[i - 2] > nums2[j - 1]) {
                        return (double) (nums1[i - 1] + nums1[i - 2]) / 2.0; 
                    } else {
                        return (double) (nums1[i - 1] + nums2[j - 1]) / 2.0;
                    }
                } else {
                    if (nums2[j - 2] > nums1[i - 1]) {
                        return (double) (nums2[j - 1] + nums2[j - 2]) / 2.0; 
                    } else {
                        return (double) (nums1[j - 1] + nums2[i - 1]) / 2.0;
                    }
                }
            } else if (i > 1 && j <= 1) {
                j = Math.max(j - 1, 0);
                if (nums1[i - 1] > nums2[j]) {
                    if (nums1[i - 2] > nums2[j]) {
                        return (double) (nums1[i - 1] + nums1[i - 2]) / 2.0;
                    }
                }
                return (double) (nums1[i - 1] + nums2[j]) / 2.0;
            } else if (j > 1 && i <= 1) {
                i = Math.max(i - 1, 0);
                if (nums2[j - 1] > nums1[i]) {
                    if (nums2[j - 2] > nums1[i]) {
                        return (double) (nums2[j - 1] + nums2[j - 2]) / 2.0;
                    }
                }
                return (double) (nums2[j - 1] + nums1[i]) / 2.0;
            } else {
                i = Math.max(i - 1, 0);
                j = Math.max(j - 1, 0);
                return (double) (nums1[i] + nums2[j]) / 2.0; 
            }
        } else {
            int i = 0, j = 0;
            while (n > med) {
                if (i < nums1.length && j < nums2.length) {
                    if (nums1[i] <= nums2[j]) ++i;
                    else ++j;
                } else if (i >= nums1.length && j < nums2.length) {
                    ++j;
                } else {
                    ++i;
                }
                --n;
            }
            i = Math.max(i - 1, 0);
            j = Math.max(j - 1, 0);
            return nums1[i] > nums2[j] ? nums1[i] : nums2[j];
        }
    }
 */
