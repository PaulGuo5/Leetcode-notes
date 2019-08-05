class Solution:
    def climbStairs1(self, n: int) -> int:
        # time exceeds
        if n <= 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        res = [0]*n
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
    
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = 2
        pre = 1
        for i in range(2, n):
            # tmp = res
            # res = pre + res
            # pre = tmp
            res, pre = pre+res, res
        return res
            
