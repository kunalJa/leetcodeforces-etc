/*
 * Accepted
 * Time Complexity : O(n).
 * Space Coplexity : O(n).
 */

/**
 * Given a string S, return the "reversed" string where all characters that are not a
 * letter stay in the same place, and all letters reverse their positions.
 * 
 *  Example 1:
 *  Input: "ab-cd"
 *  Output: "dc-ba"
 *  
 *  Example 2:
 *  Input: "a-bC-dEf-ghIj"
 *  Output: "j-Ih-gfE-dCba"
 *  
 *  Example 3:
 *  Input: "Test1ng-Leet=code-Q!"
 *  Output: "Qedo1ct-eeLg=ntse-T!"
 */

package LeetCode.easy;

import java.util.Stack;

public class Reverse_only_letters {
    /* Stack implementation. */
    public String reverseOnlyLetters(String S) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if((c >= 65 && c < 91) || c >= 97 && c < 123) {
                stack.push(c);
            }
        }
        
        StringBuilder reversed = new StringBuilder();
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if((c >= 65 && c < 91) || c >= 97 && c < 123) {
                reversed.append(stack.pop());
            } else {
                reversed.append(c);
            }
        }
        return reversed.toString();
    }
    
    /* Reverse pointer implementation. */
    public String reverseOnlyLettersPTR(String S) {
        StringBuilder ans = new StringBuilder();
        int j = S.length() - 1;
        for (int i = 0; i < S.length(); ++i) {
            if (Character.isLetter(S.charAt(i))) {
                while (!Character.isLetter(S.charAt(j)))
                    j--;
                ans.append(S.charAt(j--));
            } else {
                ans.append(S.charAt(i));
            }
        }

        return ans.toString();
   }
}
