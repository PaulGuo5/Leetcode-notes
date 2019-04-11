class Solution:
    def repeatedSubstringPattern2(self, s: str) -> bool:
        len_ = len(s)
        k = 2
        while len_ // k >= 1:
            if len_ % k != 0:
                k += 1
                continue
            if s == s[0:len_//k] * k:
                return True
            k+=1
        return False
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
