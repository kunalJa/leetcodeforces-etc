"""
https://leetcode.com/problems/diameter-of-binary-tree/

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(n)
Solution Explanation:
    The longest path through the any node:
         1 + longest path in the left subtree + longest path in right subtree
    We recurse through our tree keeping track of the longest path through every node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_num_vertices = 1

        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0
            max_height_left = dfs(root.left)
            max_height_right = dfs(root.right)
            self.max_num_vertices = max(
                self.max_num_vertices, 1 + max_height_left + max_height_right
            )
            return 1 + max(
                max_height_left, max_height_right
            )  # Add 1 to include root to the height

        dfs(root)
        return self.max_num_vertices - 1
