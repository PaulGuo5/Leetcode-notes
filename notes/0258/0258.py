class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            cnt = 0
            for d in str(num):
                cnt += int(d)
            num = cnt
        return num
