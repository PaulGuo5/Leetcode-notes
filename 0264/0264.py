class Solution:
    def ugly(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        if n != 1:
            return False
        return True
    
    def nthUglyNumber1(self, n: int) -> int:
        res = -1
        while n > 0:
            if self.ugly(res):
                n -= 1
                if n == 0:
                    break
            res += 1
        return res
    
    
    def nthUglyNumber(self, n: int) -> int:
        if n < 1:
            return 0
        u = [1] * n
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            u[i] = min(u[i2]*2, u[i3]*3, u[i5]*5)
            if u[i] == u[i2]*2:
                i2 += 1
            if u[i] == u[i3]*3:
                i3 += 1
            if u[i] == u[i5]*5:
                i5 += 1
        return u[-1]
        
        
        
        
        
        
        
