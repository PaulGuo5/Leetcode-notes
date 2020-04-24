class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            i += 1
            m >>= 1
            n >>= 1
        return n << i
