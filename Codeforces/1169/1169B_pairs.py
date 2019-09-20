"""
https://codeforces.com/contest/1169/problem/B

Toad Ivan has m pairs of integers, each integer is between 1 and n, inclusive.
The pairs are (a1, b1), (a2, b2), …, (am, bm).

He asks you to check if there exist two integers x and y (1≤x<y≤n)
such that in each given pair at least one integer is equal to x or y.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explantion:
    No matter what, the solution will contain an x or y from the first pair.
    Then we look for the first pair that does not contain that x or y and check to see
    if the elements of that pair (x1, y1) satisfy the condition that each other pair
    has one of (x or (x1 or y1)) or (y or (x1 or y1)).
"""
from sys import stdin, stdout


def find_union_universal_vertex(edges) -> str:
    def edge_to_x_or_y(x: int, y: int) -> bool:
        """Check whether or not every edge contains either x or y"""
        for edge in edges:
            if edge[0] != x and edge[0] != y and edge[1] != x and edge[1] != y:
                return False

        return True

    for x in edges[0]:
        # Perhaps every node contains x, then we are done
        if edge_to_x_or_y(x, 0):
            return "YES"

        # Searching for an edge that does not contain x
        for edge in edges:
            if edge[0] != x and edge[1] != x:
                if edge_to_x_or_y(x, edge[0]) or edge_to_x_or_y(x, edge[1]):
                    return "YES"
                break

    return "NO"


def dp_probability_rule_of_sum(value_upperbound: int, edges) -> str:
    """
    Time Limit Exceeded
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    Solution Explantion:
        The generalized rule of sums is defined as: P(A U B) = P(A) + P(B) - P(AB).
        We count the number of occurences of each value and pair in the edge list.
        We then use the sums formula to count the number of appearences of A U B.
        If that number equals the number of edges, then we have found a solution.
    """
    dp = [[0 for _ in range(value_upperbound + 1)] for _ in range(value_upperbound + 1)]
    for pair in edges:
        if pair[0] == pair[1]:
            dp[pair[0]][pair[0]] += 1
        else:
            dp[pair[0]][pair[0]] += 1
            dp[pair[1]][pair[1]] += 1
            dp[pair[0]][pair[1]] += 1
            dp[pair[1]][pair[0]] += 1

    for i in range(value_upperbound):
        for j in range(i + 1, value_upperbound):
            if dp[i][i] + dp[j][j] - dp[i][j] == len(edges):
                return "YES"

    return "NO"


if __name__ == "__main__":
    value_upperbound, n = map(int, stdin.readline().rstrip().split(" "))
    pairs = []
    for _ in range(n):
        line = stdin.readline().rstrip().split(" ")
        pairs.append([int(line[0]), int(line[1])])
    # stdout.write(dp_probability_rule_of_sum(value_upperbound, pairs) + "\n")
    stdout.write(find_union_universal_vertex(pairs) + "\n")
