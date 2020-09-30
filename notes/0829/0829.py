class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        for k in range(1, math.ceil((2*N)**0.5)):
            if (N-k*(k+1)//2) % k == 0:
                res += 1
        return res
