class Solution:
    def trailingZeroes1(self, n: int) -> int:
        #Time exceed
        def helper(n):
            if n == 1 or n == 0:
                return 1
            return n*helper(n-1)
        cnt = 0
        for c in str(helper(n))[::-1]:
            if c == "0":
                cnt += 1
            else:
                break
        return cnt
    
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n // 5
            n /= 5
        return int(res)
