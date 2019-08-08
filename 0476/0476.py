class Solution:
    def findComplement(self, num: int) -> int:
        digit = 0
        while num >= 2 ** digit:
            digit += 1
        return 2** digit - 1 -num
