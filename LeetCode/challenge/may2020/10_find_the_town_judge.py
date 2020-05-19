"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person
labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.
"""

"""
Accepted
Time complexity: O(n)
Space complexity: O(n)
Solution:
    The town judge trusts no one -> The judge's id doesn't appear on left of trust[i] = [a,b].
    Everybody trusts the judge -> Every other townsperson appears on left of trust[i].
    Then we simply need to find what number does not appear on left of trust[i].
    After we find this prospective judge, we still need to make sure that constraint 2 is met.
"""

class Solution:
    def findJudge(self, N: int, trust) -> int:
        seen = set()
        for a, b in trust:
            seen.add(a)

        prospective_judge = N * (N + 1) // 2
        for townsperson in seen:
            prospective_judge -= townsperson

        # judge = 0 when all townspeople + judge appear on left, judge > N when townspeople missing on left
        if prospective_judge == 0 or prospective_judge > N:
            return -1

        # Check constraing two: Everybody (except for the town judge) trusts the town judge.
        for a, b in trust:
            if b == prospective_judge:
                seen.remove(a)

        return prospective_judge if not seen else -1
