"""
https://leetcode.com/problems/univalued-binary-tree/

A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    Recursion.
    A unival tree has its root value equal to its left and right children's values.
    Further a unival tree has both its left subtree and its right subtree being unival.
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        if self.isUnivalTree(root.left) and self.isUnivalTree(root.right):
            return True
        return False

    def isUnivalIterative(self, root: TreeNode) -> bool:
        """
        Accepted
        Time Complexity: O(n)
        Space Complexity: O(n)
        Solution Explanation:
            BFS through the entire tree and compare the value of each node to the unival.
        """
        if root is None:
            return False

        children = deque()
        unival = root.val
        children.append(root)
        while children:
            consider = children.popleft()
            if consider:
                if consider.val != unival:
                    return False
                children.append(consider.left)
                children.append(consider.right)
        return True
