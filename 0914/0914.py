class Solution:
    def hasGroupsSizeX1(self, deck: List[int]) -> bool:
        c = collections.Counter(deck)
        d = min(c.values())
        if d < 2:
            return False
        for i in range(2, d+1):
            if all(val % i == 0 for val in c.values()):
                return True
        return False
    
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if a % b == 0: return b
            return gcd(b, a % b)
        c = collections.Counter(deck)
        vals = list(c.values())
        res = vals[0]
        for i in range(1, len(vals)):
            res = gcd(vals[i], res)
        return res >= 2
