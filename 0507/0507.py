import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        res = 0
        for n in range(1, int(math.sqrt(num))+1):
            q, r = divmod(num, n)
            if r == 0:
                res += q+n
        if num == int(math.sqrt(num)) ** 2: res -= int(math.sqrt(num))
        return True if res - num == num else False
