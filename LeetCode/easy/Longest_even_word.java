/*
 * Accepted
 * Time Complexity : O(n).
 * Space Complexity : O(1).
 */

/**
 * You are given a 
 */

package LeetCode.easy;

public class Longest_even_word {
    public static String longestEvenWord(String sentence) {
        int maxLen = 0;
        int indexOfString = -1;
        int start = 0;
        int end = 0;
        while (start < sentence.length() && end < sentence.length()) {
            if (sentence.charAt(end) == ' ') {
                int len = end - start;
                if (len % 2 == 0) {
                    if (len > maxLen) {
                        maxLen = len;
                        indexOfString = start;   
                    }
                }
                start = end + 1;
            }
            end++;
        }
        int len = end - start;
        if (len % 2 == 0) {
            if (len > maxLen) {
                maxLen = len;
                indexOfString = start;   
            }
        }
        if (indexOfString == -1)
            return "00";
        return sentence.substring(indexOfString, Math.min((indexOfString + maxLen), sentence.length()));
    }
}
