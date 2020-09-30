class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isValid(n):
            for c in str(n):
                if c == "0": return False
            return True
        
        for i in range(1, n):
            if isValid(i) and isValid(n-i):
                return [i, n-i]
