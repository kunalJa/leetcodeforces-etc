/*
 * Accepted
 * Time complexity : O(max(m,n)). 
 *      Assume that m and n represents the length of l1 and l2 respectively,
 *      the algorithm above iterates at most max(m,n) times.
 * Space complexity: O(max(m,n)).
 *      The length of the new list is at most max(m,n) + 1.
 */

/**
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * 
 *  Example:
 *  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 *  Output: 7 -> 0 -> 8
 *  Explanation: 342 + 465 = 807.
 */

package LeetCode.medium;

public class Add_two_numbers {
    private class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
   }
 
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null; 
        int carry = 0;
        ListNode sum_dummy = new ListNode(0);
        ListNode current = sum_dummy;
        while(l1 != null || l2 != null) {
            current.next = new ListNode(0);
            current = current.next;
            if (l1 == null && l2 != null) {
                current.val = l2.val + carry;
                if (current.val >= 10) {
                    carry = 1;
                    current.val -= 10;
                } else {
                    carry = 0;
                }
                l2 = l2.next;
            } else if (l2 == null && l1 != null) {
                current.val = l1.val + carry;
                if (current.val >= 10) {
                    carry = 1;
                    current.val -= 10;
                } else  {
                    carry = 0;
                }
                l1 = l1.next;
            } else {
                current.val = l1.val + l2.val + carry;
                if (current.val >= 10) {
                    carry = 1;
                    current.val -= 10;
                } else {
                    carry = 0;
                }
                l1 = l1.next;
                l2 = l2.next;
            }
        }
        if (carry > 0) { // Last value could overflow
            current.next = new ListNode(carry);
        }
        return sum_dummy.next;
    }
}

/* LeetCode's solution is a bit more optimized than mine,
 * I think for best performance its best to avoid if statements
 * unless the if statements add clarity.
 *
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;            // ternary operators so sum doesn't need ifs
            int sum = carry + x + y;
            carry = sum / 10;                           // always either 1 or 0
            curr.next = new ListNode(sum % 10);         // doesn't subtract the 10 like i do
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
*/