class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        current = ["1"]
        for i in range(1, n):
            current = []
            repeated = 1
            last_char = prev[0]
            for j in range(1,len(prev)):
                if prev[j] == last_char:
                    repeated += 1
                else:
                    current += str(repeated) 
                    current += last_char
                    repeated = 1
                last_char = prev[j]
            current += str(repeated) 
            current += last_char    
            prev = "".join(current)
            
        return "".join(current)