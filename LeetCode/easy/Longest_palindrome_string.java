/*
 * Accepted
 * Time Complexity : O(N^3)
 * Space Complexity : O(1)
 */
/**
 * Find the longest palindrome substring in a string.
 * 
 *  Example:
 *  Input: "I went to my gym yesterday"
 *  Output: " my gym "
 *      Explanation: Skip external spaces, but internal spaces are allowed.
 */

package LeetCode.easy;

public class Longest_palindrome_string {
    public static String longest_palindrome(String input) {
        int start, end, tempStart, tempEnd;
        boolean palindromeFound;
        int myPalindromeStart = 0;
        int myPalindromeEnd = -1; // Ensures return of "" with substring.
        for (start = 0; start < input.length(); start++) {
            char findMe = input.toUpperCase().charAt(start);
            for (end = input.length() - 1; end > start; end--) {
                palindromeFound = true;
                char current = input.toUpperCase().charAt(end); 
                if ((end - start + 1) >= 2 && findMe == current) { // Don't ignore spaces external to a palindrome.
                    for (tempStart = start, tempEnd = end; tempStart <= tempEnd;
                         tempStart++, tempEnd--) {
                        char leftToRight = input.toUpperCase().charAt(tempStart);
                        char rightToLeft = input.toUpperCase().charAt(tempEnd);
                        if (leftToRight == ' ') { // Ignore spaces internal to a palindrome.
                            tempEnd++;
                        } else if (rightToLeft == ' ') {
                            tempStart--;
                        } else {
                            if (leftToRight != rightToLeft) {
                                palindromeFound = false;
                            }
                        }
                    }
                    
                    if (palindromeFound) {
                        if ((end - start) > (myPalindromeEnd - myPalindromeStart)) { // Update max len palindrome.
                            myPalindromeStart = start;
                            myPalindromeEnd = end;
                        }
                    }
                }
            }
        }
        return input.substring(myPalindromeStart, myPalindromeEnd + 1); // Substring does not include the upper bound.
    }
}
