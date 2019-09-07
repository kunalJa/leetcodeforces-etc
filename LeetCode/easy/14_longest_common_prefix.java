/*
 * Accepted
 * Time Complexity : O(S) where S is the sum of all characters in all strings.
 * Space Complexity : O(1).
 */

/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 * 
 *  Example 1:
 *  Input: ["flower","flow","flight"]
 *  Output: "fl"
 *  
 *  Example 2:
 *  Input: ["dog","racecar","car"]
 *  Output: ""
 *      Explanation: There is no common prefix among the input strings.
 */

package LeetCode.easy;

public class Longest_common_prefix {
    /* This is a vertical scan approach. */
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = "";
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].length() == i || strs[j].charAt(i) != c) {
                    return prefix;
                }
            }
            prefix += c;
        }
        return prefix;
    }
}
