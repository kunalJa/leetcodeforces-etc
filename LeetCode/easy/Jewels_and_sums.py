class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        hist = [0] * 59 # Using knowledge about ascii table
        for char in S:
            hist[ord(char) - 65] += 1
        for char in J:
            count += hist[ord(char) - 65]
        return count

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for char in S:
            if char in J:
                count += 1
        return count

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 for char in S if char in J)

'''
	The 'in' operator: e in L -> L.__containts__(e)
	https://wiki.python.org/moin/TimeComplexity
'''