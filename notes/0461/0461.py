class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        while x > 0 or y > 0:
            if x&1 != y&1:
                dis += 1
            x = x >> 1
            y = y >> 1
            if x <= 0:
                x = 0
            if y <= 0:
                y = 0
        return dis