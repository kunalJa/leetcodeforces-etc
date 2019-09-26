"""
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
Note:
    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h
    is the height of the tree. You may also assume that next() call will always be valid,
    that is, there will be at least a next smallest number in the BST when next() is called.
"""

"""
Accepted
Time Complexity: O(1) on average
Space Complexity: O(h)
Solution Explanation:
    A BST maintains the invariant that all nodes in a roots left subtree are smaller
    than the root's val and all nodes in the right subtree are larger than the root's val.
    Using this idea, we always try to go to the left most node first as it is the smallest.
    If a node has no right subtree, then we know to go up a level.
    We continue going up levels while we are the right child of our parent, as being
    the right child means we are larger than our parent.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.current = root
        while self.current and self.current.left:
            self.stack.append(self.current)
            self.current = self.current.left

    def __is_left_child(self) -> bool:
        if self.current == self.stack[-1].left:
            return True
        else:
            return False

    def __is_right_child(self) -> bool:
        return not self.__is_left_child()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        smallest = self.current.val

        if self.current.right:
            self.stack.append(self.current)
            self.current = self.current.right
            while self.current.left:
                self.stack.append(self.current)
                self.current = self.current.left
        else:
            while self.stack and self.__is_right_child():
                self.current = self.stack.pop()

            if self.stack:
                self.current = self.stack.pop()
            else:
                self.current = None

        return smallest

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.current is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
