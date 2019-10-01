"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given a binary tree, determine if it is a complete binary tree.

In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    BFS.
    Keep track that you always pop left then right from the same parent.
    If ever you skip a parent on the same level, then the tree is not complete.
    If ever you pop a right node first, then the tree is not complete.
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        children = deque()
        children.append(root)
        while children:
            next_level = []
            while children:  # Distinguish between levels of the tree
                current = children.popleft()
                if current is None:
                    if len(children) > 0:
                        return False
                    # This for loop runs only once- the runtime does not become quadratic.
                    for val in next_level:
                        if val is not None:
                            return False
                    return True

                next_level.append(current.left)
                next_level.append(current.right)

            flag = False
            for node in next_level:
                if node is not None:
                    if flag:
                        return False
                    children.append(node)
                else:
                    if not flag:
                        children.append(None)
                        flag = True

        return True
