class Solution:
    def reverseStr1(self, s: str, k: int) -> str:
        res = ""
        for i in range(0, len(s), k):
            idx = min(i+k, len(s))
            if (i//k) & 1 == 0:
                res += s[i:idx][::-1]
            else:
                res += s[i:idx]
        return res
    
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
