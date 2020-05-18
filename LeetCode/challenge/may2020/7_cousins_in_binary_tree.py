"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

Two nodes of a binary tree are cousins if they have the same depth,
but have different parents.

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

"""
Time complexity: O(n)
Space complexity: O(n)
    Note that the BFS complexity is different for a tree than for a general graph.
    A tree structure -> no need to maintain a visited set of vertices.
    Further, the number of edges = O(vertices).
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent = y_parent = None
        x_depth = y_depth = 0
        depth = 0

        nodes = deque([(root, root), (None, None)])  # (0,0) marks the end of each level
        while nodes:
            current, parent = nodes.popleft()
            if parent == None:
                depth += 1
                if len(nodes) > 0:  # there are still tree nodes to check
                    nodes.append((None, None))
                continue
            if current.val == x:
                x_parent = parent
                x_depth = depth
            if current.val == y:
                y_parent = parent
                y_depth = depth
            if current.left:
                nodes.append((current.left, current))
            if current.right:
                nodes.append((current.right, current))

        return (
            x_parent
            and y_parent
            and x_parent.val != y_parent.val
            and x_depth == y_depth
        )
