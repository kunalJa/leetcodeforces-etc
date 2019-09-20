"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(n)
Solution Explanation:
    Breadth first traversal of the tree, finds the smallest node value that is larger
    than the root (because the root is garunteed to be <= all other nodes).
"""

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

        squeeze = float("inf")
        Q = deque()
        Q.append(root)

        while len(Q) > 0:
            current = Q.popleft()
            if root.val < current.val < squeeze:
                squeeze = current.val
            if current.left is not None:
                Q.append(current.left)
                Q.append(current.right)

        return -1 if squeeze == float("inf") else squeeze
