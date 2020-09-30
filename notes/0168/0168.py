class Solution:
    def convertToTitle1(self, n: int) -> str:
        dict_ = {}
        for i in range(26):
            dict_[i+1] = chr(ord("A")+i)
        dict_[0] = "Z"
        res = ""
        while n > 0:
            n, q = divmod(n, 26)
            if q == 0:
                n-=1
            res += dict_[q]
        return res[::-1]
    
    def convertToTitle(self, n: int) -> str:
        lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        while n:
            n, r = divmod(n-1, 26)
            res.append(lookup[r])
        return "".join(res[::-1])
