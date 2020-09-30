class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend>0) is (divisor>0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = divisor
            i = 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if not positive: res = -res
        return min(max(res, -2**31), 2**31-1)
