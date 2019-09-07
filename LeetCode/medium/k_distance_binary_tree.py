# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # The only solution I can think of is a full BFS from target, except we don't have parent pointers...
        adjacency_list = {}
        recursion = [root]
        # build the adjacency list
        while recursion:
            current = recursion.pop()
            if current.val not in adjacency_list:
                adjacency_list[current.val] = set()

            if current.left is not None:
                if current.left.val not in adjacency_list:
                    adjacency_list[current.left.val] = set()
                recursion.append(current.left)
                adjacency_list[current.val].add(current.left.val)
                adjacency_list[current.left.val].add(current.val)

            if current.right is not None:
                if current.right.val not in adjacency_list:
                    adjacency_list[current.right.val] = set()
                recursion.append(current.right)
                adjacency_list[current.val].add(current.right.val)
                adjacency_list[current.right.val].add(current.val)

        # for k, v in adjacency_list.items():
        #     print(f'{k} {[x for x in v]}')

        # BFS
        next_node = deque()
        seen = set()
        level = 0
        next_node.append((target.val, level))
        while next_node:
            current = next_node.popleft()
            seen.add(current[0])
            level = current[1]
            if level == K:
                return [x[0] for x in next_node if x[1] == K] + [current[0]]
            else:
                for child in adjacency_list[current[0]]:
                    if child not in seen:
                        next_node.append((child, level + 1))

        return[]
