"""
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false

Example 2:
    Input: 1->2->2->1
    Output: true
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Iterate to the center, reversing the linked list along the way.
    Now split into 2 pointers and iterate in reverse on the left and forward on the right.
    Compare each character to ensure the list is a palindrome.
    i.e.
        1 -> 2 -> 2 -> 3 -> 2 -> 2 -> 1 becomes
        1 <- 2 <- 2 <- 3 -> 2 -> 2 -> 1
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        n = 1
        prev = None
        slow = head
        following = head.next
        fast = head.next
        while fast is not None:
            slow.next = prev
            prev = slow
            slow = following
            if following is not None:
                following = following.next

            fast = fast.next
            n += 1
            if fast is not None:
                n += 1
                fast = fast.next

        # If there are an odd number of elements, skip the center element.
        if n % 2 != 0:
            slow = following

        while slow is not None and prev is not None:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next

        return True
