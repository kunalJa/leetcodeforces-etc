/*
 * Couldn't quite solve it in exactly 1 pass. Solution below is thanks to Leet Code.
 * 
 * Sliding Window:
 * 
 * The trick they use to not have to make a new HashMap is that they take the max of 
 * their start index and the index of the repeated character in the set (the old one).
 * This way they can ignore the fact that the repeated character may be out of bounds of
 * their "window." 
 * They then always add the current (end) character value to the map. This also updates
 * old repeated characters. This updating is important! (the + 1 is important too).
 * 
 * Time complexity : O(n). 
 *      The function makes one pass through the characters of the string.
 * Space complexity: O(n).
 *      We put every character into the hash map. Duplicates won't be added, but the worst
 *      case is that every character is different.
 */

/**
 * Given a string, find the length of the longest substring without repeating characters.
 *  Example 1:
 *  Input: "abcabcbb"
 *  Output: 3 
 *  Explanation: The answer is "abc", with the length of 3. 
 *  
 *  Example 2:
 *  Input: "bbbbb"
 *  Output: 1
 *  Explanation: The answer is "b", with the length of 1.
 *  
 *  Example 3:
 *  Input: "pwwkew"
 *  Output: 3
 *  Explanation: The answer is "wke", with the length of 3.
 *Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */

package LeetCode.medium;

import java.util.HashMap;

public class Longest_substring_without_repeating_characters {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), maxLen = 0;
        HashMap<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int start = 0, end = 0; end < n; end++) {
            if (map.containsKey(s.charAt(end))) {
                start = Math.max(map.get(s.charAt(end)), start);
            }
            maxLen = Math.max(maxLen, end - start + 1);
            map.put(s.charAt(end), end + 1);
        }
        return maxLen;
    }
}

/*
 * Accepted
 * My initial solution ->
 * Its close, but it has the potential to unnecessarily iterate
 * over the same variable many times. Take for example string "abcdabcdabcd"
 * It seems to approach O(n^2) runtime but i'm not quite sure.
 * Its space complexity is O(n). Although, i'm unsure how repeated new 
 * hash maps of size k where k is the current substring length affects the space.
 * In essence though, there is at most every character in the hash map.
 *      
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        for (int i = 0; i < s.length(); i++) {
            HashMap<Character, Integer> seen = new HashMap<>();
            int currLen = 0;
            while(i < s.length() && !seen.containsKey(s.charAt(i))) {
                currLen++;
                seen.put(s.charAt(i), i);
                ++i;
            }
            if (i < s.length()) i = seen.get(s.charAt(i));
            maxLen = currLen > maxLen ? currLen : maxLen;
        }
        return maxLen;
    }
 */

