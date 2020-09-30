class Solution:
    def reverse1(self, x: int) -> int:
        str_ = str(abs(x))[::-1]
        if int(str_) > (2**31-1): return 0
        return int(str_) if x > 0 else -int(str_)

    
    def reverse(self, x: int) -> int:
        if x < 0: return - self.reverse(-x)
        res = 0
        while x > 0:
            res = res*10 + x % 10
            x //= 10
            if res > 2**31:
                return 0
        return res