/*
 * Accepted
 * Time Complexity : O(n).
 * Space Complexity : O(1).
 */

/**
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
 *      Symbol       Value
 *      I             1
 *      V             5
 *      X             10
 *      L             50
 *      C             100
 *      D             500
 *      M             1000
 * For example, two is written as II in Roman numeral, just two one's added together.
 * Twelve is written as, XII, which is simply X + II. The number twenty seven is written
 * as XXVII, which is XX + V + II. Roman numerals are usually written largest to smallest
 * from left to right. However, the numeral for four is not IIII. 
 * Instead, the number four is written as IV. Because the one is before 
 * the five we subtract it making four. The same principle applies to the number nine,
 * which is written as IX. There are six instances where subtraction is used:
 *      I can be placed before V (5) and X (10) to make 4 and 9. 
 *      X can be placed before L (50) and C (100) to make 40 and 90. 
 *      C can be placed before D (500) and M (1000) to make 400 and 900.
 *      
 *Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
 */

package LeetCode.easy;

import java.util.HashMap;

public class Roman_to_integer {
    public int romanToInt(String s) {
        int val = 0;
        boolean I = false, X = false, C = false;
        @SuppressWarnings("serial")
        HashMap<Character, Integer> symbolTable = new HashMap<Character, Integer>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (I && (current == 'V' || current == 'X')) {
                val -= 2;
                I = false;
            } else if (X && (current == 'L' || current == 'C')) {
                val -= 20;
                X = false;
            } else if (C && (current == 'D' || current == 'M')) {
                val -= 200;
                C = false;
            }
            
            if (current == 'I') {
                I = true;
            }
            else if (current == 'X') {
                X = true;
            }
            else if (current == 'C') {
                C = true;
            } else {
                I = false;
                X = false;
                C = false;
            }
            
            val += symbolTable.get(current);
        }
        return val;
    }
}
