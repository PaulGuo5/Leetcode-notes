class Solution:
    def judgeSquareSum1(self, c: int) -> bool:
        def is_square(n):
            return int(n**0.5)**2 == n
        return any(is_square(c-a*a) for a in range(int(c**0.5)+1))
    
    def judgeSquareSum(self, c: int) -> bool:
        high = 0
        while high*high < c:
            high += 1
        low = 0
        while low <= high:
            if low**2+high**2 == c:
                return True
            if low**2+high**2 < c:
                low += 1
            if low**2+high**2 > c:
                high -= 1
        return False
