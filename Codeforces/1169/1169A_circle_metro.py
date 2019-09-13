"""
https://codeforces.com/contest/1169/problem/A

The circle line of the Roflanpolis subway has n stations.

There are two parallel routes in the subway.
The first one visits stations in order 1 -> 2 -> … -> n -> 1 -> 2 -> …
The second route visits stations in order n -> n−1 -> … -> 1 -> n -> -> …
All trains depart their stations simultaneously, and it takes exactly 1 minute to arrive at the
next station.
Two toads live in this city, their names are Daniel and Vlad.
Daniel is currently in a train of the first route at station a and will exit the
subway when his train reaches station x.
Coincidentally, Vlad is currently in a train of the second route at station b
and he will exit the subway when his train reaches station y.

All numbers a, x, b, y are distinct.

Toad Ilya asks you to check if Daniel and Vlad will ever be at the same station at
the same time during their journey. In other words, check if there is a moment when
their trains stop at the same station.
Note that this includes the moments whenDaniel or Vlad enter or leave the subway.
"""

"""
Accepted
Time Complexity: O(n)
Space Complexity: O(1)
Solution Explanation:
    Simply iterate through the stations as the trains move at the same speed.
    Check whether or not vlad and daniel meet.
"""
from sys import stdin, stdout


def when_daniel_met_vlad(
    num_stations: int, daniel: int, daniel_end: int, vlad: int, vlad_end: int
) -> str:
    daniel_reached = False
    vlad_reached = False
    while not daniel_reached or not vlad_reached:
        if daniel == vlad:
            return "YES"
        if not daniel_reached:
            daniel = max(1, (daniel + 1) % (num_stations + 1))
            daniel_reached = daniel == daniel_end
        else:
            daniel = num_stations + 1  # Daniel has left the station
        if not vlad_reached:
            vlad = (vlad - 1) if vlad != 1 else num_stations
            vlad_reached = vlad == vlad_end
        else:
            vlad = num_stations + 1  # Vlad has left the station

    return "NO"


if __name__ == "__main__":
    n, a, x, b, y = map(int, stdin.readline().rstrip().split(" "))
    stdout.write(when_daniel_met_vlad(n, a, x, b, y) + "\n")
