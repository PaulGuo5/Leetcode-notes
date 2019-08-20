class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0 or n==1:
            return True
        def dec2bin(num):
            l = []
            if num < 0:
                return '-' + dec2bin(abs(num))
            while True:
                num, remainder = divmod(num, 2)
                l.append(str(remainder))
                if num == 0:
                    return l[::-1]
        pre = 0
        n = dec2bin(n)
        for i in range(1, len(n)):
            if n[i] == n[pre]:
                return False
            pre = i
        return True
