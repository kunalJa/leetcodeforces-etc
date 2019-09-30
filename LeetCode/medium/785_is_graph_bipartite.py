"""
https://leetcode.com/problems/is-graph-bipartite/

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent
subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form:
    graph[i] is a list of indexes j for which the edge between nodes i and j exists.

Each node is an integer between 0 and graph.length - 1.
There are no self edges or parallel edges: graph[i] does not contain i
Further, it doesn't contain any element twice.
"""

"""
Accepted
Time Complexity: O(V + E)
Space Complexity: O(V)
Solution Explanation:
    DFS over the graph marking each node as you go in an alternating fashion.
    If ever you visit a node you have previously and attempt to mark it a different
    color than it was originally marked, return False.
"""
from typing import Set, List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs_search(G: List[List[int]], v: int, color: bool, red: Set, blue: Set):
            color ^= True
            if color:
                if v in red:  # We cannot 2 color the graph
                    return False
                elif v in blue:  # We have already seen this node
                    return True
                blue.add(v)
            else:
                if v in blue:  # We cannot 2 color the graph
                    return False
                elif v in red:  # We have already seen this node
                    return True
                red.add(v)

            for adjacent in G[v]:
                if not dfs_search(G, adjacent, color, red, blue):
                    return False
            return True

        red = set()
        blue = set()
        for v in range(len(graph)):
            if v not in blue and v not in red:
                if not dfs_search(graph, v, True, red, blue):
                    return False

        return True
