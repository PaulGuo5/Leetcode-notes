class Solution:
    def findNthDigit(self, n: int) -> int:
        len_, start, cnt = 1, 1, 9
        while n > len_*cnt:
            n -= len_*cnt
            len_ += 1
            cnt *= 10
            start *= 10
        start += (n - 1) // len_
        return int(str(start)[(n - 1) % len_])
