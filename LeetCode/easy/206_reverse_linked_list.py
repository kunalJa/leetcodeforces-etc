"""
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Use three pointers (prev, current, and next) to reverse the linked list as you iterate.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            if next is not None:
                next = next.next

        return prev

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        """
        Accepted
        Time Complexity: O(n)
        Space Complexity: O(n)
        Solution Explanation:
            Recurse all the way to the last node.
            Then before popping off the stack, set head.next to prev.
        """

        def recurse(head: ListNode, prev: ListNode) -> ListNode:
            if head is None:
                return prev
            new_head = recurse(head.next, head)
            head.next = prev
            return new_head

        return recurse(head, None)
