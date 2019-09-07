class Solution:
    def rotatedDigits(self, N: int) -> int:

        goodMapping = {0: 0, 1:1, 2:5, 5:2, 6:9, 8:8, 9:6}
        goodNums = 0

        for i in range(1, N + 1):
            badNum = False
            original = i
            rotated = 0
            placeValue = 0

            while (i > 0):
                try:
                    rotated += (goodMapping.get(i % 10) * (10 ** placeValue))
                except:
                    badNum = True
                    break
                placeValue += 1
                i = i // 10

            if not badNum and original != rotated:
                goodNums += 1

        return goodNums
