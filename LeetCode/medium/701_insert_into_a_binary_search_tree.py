"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can return any of them.
"""

"""
Accepted
Time Complexity: O(H) where H is the height of the tree
Space Complexity: O(1)
Solution Explanation:
    Iterate through the tree moving right if the current node is smaller than val
    and left otherwise. Then, we place the new node in the most obvious place,
    as a leaf node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        while current is not None:
            if current.val < val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break

        if root:
            return root
        return TreeNode(val)
