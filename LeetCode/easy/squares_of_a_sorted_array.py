class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squaredList = []
        pos = []
        neg = []

        for x in A:
            if x >= 0:
                pos.append(x ** 2)
            else:
                neg.append(x ** 2)

        pos_i = 0
        neg_i = len(neg) - 1
        while True:
            if pos_i >= len(pos):
                while neg_i >= 0:
                    squaredList.append(neg[neg_i])
                    neg_i -= 1
                break
            if neg_i < 0:
                while pos_i < len(pos):
                    squaredList.append(pos[pos_i])
                    pos_i += 1
                break
            if pos[pos_i] <= neg[neg_i]:
                squaredList.append(pos[pos_i])
                pos_i += 1
            else:
                squaredList.append(neg[neg_i])
                neg_i -= 1

        return squaredList
