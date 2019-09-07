/*
 * Accepted -> better solution is in Two_sum_hash
 * Time complexity : O(nlgn).
 *      Sorting the array takes O(nlgn) time. We loop through the sorted array and do
 *      a binary search on for the value that would make it match the target. Then
 *      if we find it, we do one linear search on the original array copy to get its
 *      indices. Since this linear search happens only once, we are really just doing
 *      n (loop through sorted array) * lgn (binary search) + 2n (linear search).
 * Space complexity: O(n).
 *      The length of the original before sorting is copied to
 *      preserve original index locations.
 */

/**
 * Given an array of integers, return indices of the two numbers such that
 * they add up to a specific target. You may assume that each input would have
 * exactly one solution, and you may not use the same element twice.
 * 
 *  Example:
 *  Given nums = [2, 7, 11, 15], target = 9
 *  Because nums[0] + nums[1] = 2 + 7 = 9,
 *  return [0, 1].
 */

package LeetCode.easy;

import java.util.Arrays;

public class Two_sum {
    public int[] twoSum(int[] nums, int target) {
        int i, j = -1;
        int[] orig = new int[nums.length];
        
        for (int k = 0; k < nums.length; k++) {
            orig[k] = nums[k];
        }
        
        Arrays.sort(nums);
        for (i = 0; i < nums.length; i++) {
            j = binarySearch(nums, target - nums[i], i);
            if (j != -1) {
                i = findVal(orig, nums[i]);
                j = findVal(orig, nums[j], i);
                break;
            }
        }
        
        if (i > j) {
            return new int[] {j, i};
        } 
        
        return new int[] {i, j};
    }
    
    // binary search for a value other than that at index 'no'
    public static int binarySearch(int[] nums, int target, int no) {
        int mid, low = 0, high = nums.length - 1;
        
        while (low <= high) {
            mid = low + (high - low) / 2;
            if (nums[mid] == target && mid != no) {
                return mid;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return -1;
    } 
    
    // linear search
    public static int findVal(int[] arr, int val) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == val) {
                return i;
            }
        }
        
        return -1;
    }
    
    // Find a value thats not can't with linear search
    public static int findVal(int[] arr, int val, int cant) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == val && i != cant) {
                return i;
            }
        }
        
        return -1;
    }
}

/* Another Solution in O(nlogn) that takes better advantage
 * of the fact that it is a sorted array.
 
     public int[] twoSum(int[] nums, int target) {
        int[] orig_sorted = new int[nums.length];
        
        for (int k = 0; k < nums.length; k++) {
            orig_sorted[k] = nums[k];
        }
        
        Arrays.sort(orig_sorted);
        int i = 0;
        int j = orig_sorted.length - 1;
        while (i != j) {
            int sum = orig_sorted[i] + orig_sorted[j];
            if (sum == target) {
                return new int[] {findVal(nums, orig_sorted[i]), findValReverse(nums, orig_sorted[j])};
            } else if (sum > target) {
                j--;
            } else {
                i++;
            }
        }
        return new int[] {-1, -1};
     }
     
     public static int findVal(int[] arr, int val) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == val) {
                return i;
            }
        }
        return -1;
     }
    
    public static int findValReverse(int[] arr, int val) {
        for (int i = arr.length -1; i >= 0; i--) {
            if (arr[i] == val) {
                return i;
            }
        }
        return -1;
    }
 
 */  
