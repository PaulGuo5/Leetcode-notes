class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            return self.toHex(num + 2 ** 32)
        if 0 <= num < 10:
            return str(num)
        if 10 <= num < 16:
            return chr(num - 10 + ord("a"))
        return self.toHex(num//16) + self.toHex(num%16)
