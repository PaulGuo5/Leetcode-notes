class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        str_x = str_x[::-1]
        if int(str_x) > 2147483647:
            return 0
        return int(str_x) if x > 0 else -int(str_x)
