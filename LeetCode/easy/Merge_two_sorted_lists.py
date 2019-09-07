# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = ListNode(None) # dummy variable
        head = current

        while l1 is not None or l2 is not None:

            if l1 is None:
                while l2 is not None:
                    current.next = ListNode(l2.val)
                    current = current.next
                    l2 = l2.next
                break

            if l2 is None:
                while l1 is not None:
                    current.next = ListNode(l1.val)
                    current = current.next
                    l1 = l1.next
                break

            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next

            current = current.next

        return head.next

    # Iteratively 2
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedList = ListNode(None)
        head = None

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                mergedList.next = ListNode(l1.val)
                l1 = l1.next
            else:
                mergedList.next = ListNode(l2.val)
                l2 = l2.next
            if head is None:
                head = mergedList.next
            mergedList = mergedList.next

        while l1 is not None:
            mergedList.next = ListNode(l1.val)
            l1 = l1.next
            if head is None:
                head = mergedList.next
            mergedList = mergedList.next

        while l2 is not None:
            mergedList.next = ListNode(l2.val)
            l2 = l2.next
            if head is None:
                head = mergedList.next
            mergedList = mergedList.next

        return head

    # Recursively
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
