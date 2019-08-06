class Solution:
    def arrangeCoins(self, n: int) -> int:
        tmp_sum = 0
        level = 0
        for i in range(1, 2**32):
            tmp_sum += i
            level += 1
            if n == tmp_sum:
                break
            if n < tmp_sum:
                level -= 1
                break
        return level
