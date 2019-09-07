# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # Tree given is non-empty
        # Tree is full
        # Any node's value is less than or equal to its children
        
        squeeze = float('inf')
        Q = deque()
        Q.append(root)
        
        while len(Q) > 0:
            current = Q.popleft()
            if root.val < current.val < squeeze:
                squeeze = current.val
            if current.left is not None:
                Q.append(current.left)
                Q.append(current.right)
            
        return -1 if squeeze == float('inf') else squeeze