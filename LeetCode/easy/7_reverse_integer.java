/*
 * Accepted
 * Time Complexity : O(log(x))
 *      This is because a positive number has the ⌊log(n)⌋ + 1 digits. (log base 10).
 * Space Complexity : O(1)
 */

/**
 * Given a 32-bit signed integer, reverse digits of an integer.
 * Assume we are dealing with an environment which could only store integers within
 * the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
 * assume that your function returns 0 when the reversed integer overflows.
 *  Example 1:
 *  Input: 123
 *  Output: 321
 *  
 *  Example 2:
 *  Input: -123
 *  Output: -321
 *  
 *  Example 3:
 *  Input: 120
 *  Output: 21
 */

package LeetCode.easy;

public class Reverse_integer {
    public int reverse(int x) {
        int initial = x;
        int reversed = 0;
        while (initial != 0) {
            // Check for overflow
            if (reversed > Integer.MAX_VALUE / 10)
                return 0;
            if (reversed < Integer.MIN_VALUE / 10)
                return 0;
            reversed *= 10;
            reversed += initial % 10;
            initial /= 10;
        }
        return reversed;
    }
}
