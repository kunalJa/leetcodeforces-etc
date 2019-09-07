/*
 * Accepted
 * Time complexity : O(n).
 *   We traverse the list containing n elements only once.
 *   Each look up in the table costs only O(1) time.
 * Space complexity : O(n).
 *    The extra space required depends on the number of items stored
 *    in the hash table, which stores at most n elements.
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

import java.util.HashMap;

public class Two_sum_hash {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> rest = new HashMap<>(); // Integers to indices
        for (int i = 0; i < nums.length; i++) {
            if (rest.containsKey(target - nums[i])) {
                return new int[] {rest.get(target - nums[i]), i};
            } else {
                rest.put(nums[i], i);
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
